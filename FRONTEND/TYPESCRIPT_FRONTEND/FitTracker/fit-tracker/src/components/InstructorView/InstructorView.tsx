import { useState } from "react";
import type { Instructor } from "../../types/instructor";
import type { User } from "../../types/user";
import { getInstructorWeeklySummaries } from "../../utils/fitness";
import "./InstructorView.css";

type InstructorViewProps = {
  instructors: Instructor[];
  users: User[];
};

export function InstructorView({ instructors, users }: InstructorViewProps) {
  const [selectedInstructorId, setSelectedInstructorId] = useState<number>(0);

  const selectedInstructor =
    instructors.find((instructor) => instructor.id === selectedInstructorId) ??
    null;

  const assignedUsers = selectedInstructor
    ? selectedInstructor.assignedUsers
        .map((userId) => users.find((user) => user.id === userId))
        .filter((user): user is User => user !== undefined)
    : [];

  const weeklySummaries = selectedInstructor
    ? getInstructorWeeklySummaries(selectedInstructor, users)
    : [];

  return (
    <section className="instructor-view">
      <h2>Panel de instructores</h2>

      <label htmlFor="instructor-select">Seleccionar instructor:</label>

      <select
        id="instructor-select"
        value={selectedInstructorId}
        onChange={(e) => setSelectedInstructorId(Number(e.target.value))}
      >
        <option value={0}>Seleccione un instructor</option>

        {instructors.map((instructor) => (
          <option key={instructor.id} value={instructor.id}>
            {instructor.name}
          </option>
        ))}
      </select>

      {selectedInstructor && (
        <div className="assigned-users">
          <h3>Instructor: {selectedInstructor.name}</h3>

          {assignedUsers.length === 0 ? (
            <p>Este instructor todavía no tiene usuarios asignados.</p>
          ) : (
            assignedUsers.map((user, index) => (
              <article key={user.id} className="user-summary">
                <h4>
                  {user.name} ({user.experienceLevel}){" "}
                </h4>

                <p>
                  Rutina:{" "}
                  {user.routine ? user.routine.name : "Sin rutina asignada"}
                </p>

                {weeklySummaries[index] && (
                  <div className="weekly-summary">
                    <h5>Resumen semanal</h5>

                    <p>
                      Días de entrenamiento:{" "}
                      {weeklySummaries[index].trainingDays}
                    </p>

                    <p>
                      Minutos totales: {weeklySummaries[index].totalMinutes}
                    </p>

                    <p>
                      Calorías totales: {weeklySummaries[index].totalCalories}
                    </p>

                    <div className="pending-exercises">
                      <p>
                        Ejercicios pendientes:{" "}
                        {weeklySummaries[index].pendingExercises.length}
                      </p>

                      {weeklySummaries[index].pendingExercises.length > 0 ? (
                        <ul>
                          {weeklySummaries[index].pendingExercises.map(
                            (exercise) => (
                              <li key={exercise.id}>{exercise.name}</li>
                            ),
                          )}
                        </ul>
                      ) : (
                        <p>No hay ejercicios pendientes.</p>
                      )}
                    </div>

                    {weeklySummaries[index].restRecommendation && (
                      <p>
                        Recomendación de descanso:{" "}
                        {weeklySummaries[index].restRecommendation}
                      </p>
                    )}
                  </div>
                )}
              </article>
            ))
          )}
        </div>
      )}
    </section>
  );
}
