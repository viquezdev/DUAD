import { useState } from "react";
import type { Exercise } from "../../types/exercise";
import type { RoutineEntry } from "../../types/routineEntry";
import type { WeeklyRoutine } from "../../types/weeklyRoutine";
import type { DayOfWeek } from "../../types/routineEntry";
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
  const [entries, setEntries] = useState<RoutineEntry[]>([]);
  const selectedExercise = exercises.find(
    (exercise) => exercise.name === exerciseName,
  );
  const handleAddEntry = () => {
    if (!selectedExercise || !day) {
      return;
    }

    const newEntry: RoutineEntry = {
      day,
      exercise: selectedExercise,
    };

    setEntries((currentEntries) => [...currentEntries, newEntry]);
  };
  const handleCreateRoutine = () => {
    const newRoutine: WeeklyRoutine = {
      name,
      entries,
    };
    onCreateRoutine(newRoutine);
  };
  return (
    <div className="routine-form">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          if (!name.trim() || entries.length === 0) {
            return;
          }
          handleCreateRoutine();
          setName("");
          setDay("");
          setExerciseName("");
          setEntries([]);
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
        <button type="button" onClick={handleAddEntry}>
          Agregar entrada
        </button>
        <section>
          <h3>Entradas de la rutina</h3>

          {entries.map((entry, index) => (
            <p key={index}>
              {entry.day} → {entry.exercise.name}
            </p>
          ))}
        </section>
        <button type="submit">Crear rutina</button>
      </form>
    </div>
  );
};

export default RoutineForm;
