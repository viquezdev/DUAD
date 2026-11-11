import { useState } from "react";
import type { WeeklyRoutine } from "../../types/weeklyRoutine";
import type { DayOfWeek } from "../../types/routineEntry";
import type { DaySession } from "../../types/daySession";
import type { RoutineExercise } from "../../types/routineExercise";
import type { Exercise } from "../../types/exercise";
import { calculateCalories } from "../../utils/fitness";

import "./RoutineForm.css";

type RoutineFormProps = {
  exercises: Exercise[];
  onCreateRoutine: (routine: WeeklyRoutine) => void;
};

export const RoutineForm = ({
  exercises,
  onCreateRoutine,
}: RoutineFormProps) => {
  const [name, setName] = useState<string>("");
  const [day, setDay] = useState<DayOfWeek | "">("");
  const [exerciseName, setExerciseName] = useState<string>("");
  const [daySessions, setDaySessions] = useState<DaySession[]>([]);
  const [comment, setComment] = useState<string>("");
  const selectedExercise = exercises.find(
    (exercise) => exercise.name === exerciseName,
  );
  const createRoutineExercise = (exercise: Exercise): RoutineExercise => {
    switch (exercise.category) {
      case "cardio":
        return {
          ...exercise,
          isCompleted: false,
          caloriesBurned: calculateCalories(exercise),
        };

      case "strength":
        return {
          ...exercise,
          isCompleted: false,
        };

      case "flexibility":
        return {
          ...exercise,
          isCompleted: false,
        };
    }
  };
  const handleAddExercise = () => {
    if (!selectedExercise || !day) {
      return;
    }
    const routineExercise = createRoutineExercise(selectedExercise);
    const existingSession = daySessions.find((session) => session.day === day);

    if (existingSession) {
      setDaySessions((currentSessions) =>
        currentSessions.map((session) => {
          if (session.day === day) {
            return {
              ...session,
              exercises: [...session.exercises, routineExercise],
              comment: comment.trim() ? comment : session.comment,
            };
          }

          return session;
        }),
      );
    } else {
      const newDaySession: DaySession = {
        day,
        exercises: [routineExercise],
        comment,
      };

      setDaySessions((currentSessions) => [...currentSessions, newDaySession]);
    }

    setExerciseName("");
    setComment("");
  };
  const handleCreateRoutine = () => {
    const newRoutine: WeeklyRoutine = {
      id: Date.now(),
      name,
      startDate: new Date(),
      sessions: daySessions,
    };
    onCreateRoutine(newRoutine);
  };
  return (
    <div className="routine-form">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          if (!name.trim() || daySessions.length === 0) {
            return;
          }
          handleCreateRoutine();
          setName("");
          setDay("");
          setExerciseName("");
          setDaySessions([]);
          setComment("");
        }}
      >
        <h2>Crear rutina</h2>
        <label htmlFor="routine-name">Nombre de la rutina:</label>
        <input
          type="text"
          id="routine-name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <label htmlFor="day">Día de la rutina:</label>
        <select
          id="day"
          value={day}
          onChange={(e) => setDay(e.target.value as DayOfWeek)}
        >
          <option value="">Seleccione un día</option>
          <option value="Lunes">Lunes</option>
          <option value="Martes">Martes</option>
          <option value="Miércoles">Miércoles</option>
          <option value="Jueves">Jueves</option>
          <option value="Viernes">Viernes</option>
          <option value="Sábado">Sábado</option>
          <option value="Domingo">Domingo</option>
        </select>
        <label htmlFor="routine-exercise">Ejercicio:</label>

        <select
          id="routine-exercise"
          value={exerciseName}
          onChange={(e) => setExerciseName(e.target.value)}
        >
          <option value="">Seleccione un ejercicio</option>

          {exercises.map((exercise) => (
            <option key={exercise.name} value={exercise.name}>
              {exercise.name}
            </option>
          ))}
        </select>
        <label htmlFor="routine-comment">Comentario:</label>
        <textarea
          id="routine-comment"
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          placeholder="Escribe un comentario para esta sesión..."
        />
        <button
          className="btn-session"
          type="button"
          onClick={handleAddExercise}
        >
          Agregar sesión
        </button>
        <section>
          <h3>Sesiones de la rutina</h3>
          {daySessions.map((session) => (
            <div key={session.day}>
              <h4>{session.day}</h4>

              {session.exercises.map((exercise) => (
                <p key={exercise.id}>{exercise.name}</p>
              ))}
              {session.comment && <p>{session.comment}</p>}
            </div>
          ))}
        </section>
        <button type="submit">Crear rutina</button>
      </form>
    </div>
  );
};

export default RoutineForm;
