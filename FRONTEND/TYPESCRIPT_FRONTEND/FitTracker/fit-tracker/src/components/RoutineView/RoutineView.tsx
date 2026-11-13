import type { WeeklyRoutine } from "../../types/weeklyRoutine";
import type { DayOfWeek } from "../../types/routineEntry";
import type { RoutineExercise } from "../../types/routineExercise";
import {
  calculateTotalCalories,
  calculateAverageCalories,
  calculateTrainingDays,
  findHighestCalorieDay,
} from "../../utils/fitness";
import "./RoutineView.css";

type RoutineViewProps = {
  routine: WeeklyRoutine;
  onToggleExercise: (day: DayOfWeek, exerciseId: RoutineExercise["id"]) => void;
  onUpdateSessionComment: (day: DayOfWeek, comment: string) => void;
};

function describeRoutineExercise(exercise: RoutineExercise): string {
  switch (exercise.category) {
    case "cardio":
      return `${exercise.name} [${exercise.category}], ${exercise.duration} min | ${exercise.caloriesBurned} kcal quemadas `;
    case "strength":
      return `${exercise.name} [${exercise.category}], ${exercise.duration} min | ${exercise.weight} kg levantados `;
    case "flexibility":
      return `${exercise.name} [${exercise.category}], ${exercise.duration} min `;
  }
}

export const RoutineView = ({
  routine,
  onToggleExercise,
  onUpdateSessionComment,
}: RoutineViewProps) => {
  const totalCalories = calculateTotalCalories(routine);
  const averageCalories = calculateAverageCalories(routine);
  const trainingDays = calculateTrainingDays(routine);
  const highestCalorieDay = findHighestCalorieDay(routine);
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
                  <p>{describeRoutineExercise(exercise)}</p>
                  {exercise.category === "flexibility" && exercise.comment && (
                    <p className="exercise-comment">
                      Comentario: {exercise.comment}
                    </p>
                  )}
                </label>
              </div>
            ))}
            <label>
              Comentario de la sesión:
              <input
                type="text"
                value={session.comment ?? ""}
                onChange={(e) =>
                  onUpdateSessionComment(session.day, e.target.value)
                }
                placeholder="Escribe una nota para este día..."
              />
            </label>
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
        <p>Día con más calorías: {highestCalorieDay?.day}</p>
      </div>
    </section>
  );
};
