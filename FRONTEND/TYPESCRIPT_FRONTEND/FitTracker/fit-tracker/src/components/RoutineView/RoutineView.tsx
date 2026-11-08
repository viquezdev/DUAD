import type { WeeklyRoutine } from "../../types/weeklyRoutine";
import type { DayOfWeek } from "../../types/routineEntry";
import type { RoutineExercise } from "../../types/routineExercise";

type RoutineViewProps = {
  routine: WeeklyRoutine;
  onToggleExercise: (day: DayOfWeek, exerciseId: RoutineExercise["id"]) => void;
};

export const RoutineView = ({
  routine,
  onToggleExercise,
}: RoutineViewProps) => {
  return (
    <section className="card">
      <h2>{routine.name}</h2>

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
                  {exercise.name}, {exercise.duration} min
                </label>
              </div>
            ))}

            {session.comment && <p>{session.comment}</p>}
          </div>
        );
      })}
    </section>
  );
};
