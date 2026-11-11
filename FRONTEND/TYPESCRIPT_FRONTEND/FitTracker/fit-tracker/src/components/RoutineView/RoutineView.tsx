import type { WeeklyRoutine } from "../../types/weeklyRoutine";
import type { DayOfWeek } from "../../types/routineEntry";
import type { RoutineExercise } from "../../types/routineExercise";
import {
  calculateTotalCalories,
  calculateAverageCalories,
  calculateTrainingDays,
} from "../../utils/fitness";
import "./RoutineView.css";

type RoutineViewProps = {
  routine: WeeklyRoutine;
  onToggleExercise: (day: DayOfWeek, exerciseId: RoutineExercise["id"]) => void;
};

export const RoutineView = ({
  routine,
  onToggleExercise,
}: RoutineViewProps) => {
  const totalCalories = calculateTotalCalories(routine);
  const averageCalories = calculateAverageCalories(routine);
  const trainingDays = calculateTrainingDays(routine);
  return (
    <section className="routine-view">
      <h2>Rutina: {routine.name}</h2>

      {routine.sessions.map((session) => {
        const completedExercises = session.exercises.filter(
          (exercise) => exercise.isCompleted,
        ).length;

        const pendingExercises = session.exercises.filter(
          (exercise) => !exercise.isCompleted,
        ).length;

        return (
          <div key={session.day}>
            <h3>{session.day}</h3>
            <p>Completados: {completedExercises}</p>
            <p>Pendientes: {pendingExercises}</p>

            {session.exercises.map((exercise) => (
              <div key={exercise.id}>
                <label>
                  <input
                    type="checkbox"
                    checked={exercise.isCompleted}
                    onChange={() => {
                      onToggleExercise(session.day, exercise.id);
                    }}
                  />
                  <p>
                    {exercise.name}, {exercise.duration} min
                  </p>
                </label>
              </div>
            ))}

            {session.comment && <p>{session.comment}</p>}
          </div>
        );
      })}

      <div className="weekly-summary">
        <h3>Resumen semanal</h3>
        <p>Total semanal: {totalCalories} kcal</p>
        <p>
          Promedio: {averageCalories.toFixed(2)} kcal ({trainingDays} días
          entrenados)
        </p>
      </div>
    </section>
  );
};
