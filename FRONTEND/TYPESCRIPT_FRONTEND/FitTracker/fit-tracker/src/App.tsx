import { UserForm } from "./components/UserForm/UserForm";
import type { UserFormData } from "./components/UserForm/UserForm";
import { useState } from "react";
import { ExerciseForm } from "./components/ExerciseForm/ExerciseForm";
import type { Exercise, NewExercise } from "./types/exercise";
import type { WeeklyRoutine } from "./types/weeklyRoutine";
import type { DayOfWeek } from "./types/routineEntry";
import type { RoutineExercise } from "./types/routineExercise";
import { RoutineView } from "./components/RoutineView/RoutineView";
import { WeeklyLoadView } from "./components/WeeklyLoadView/WeeklyLoadView";
import type { Instructor } from "./types/instructor";
import { InstructorForm } from "./components/InstructorForm/InstructorForm";
import type { InstructorFormData } from "./components/InstructorForm/InstructorForm";
import type { InstructorId } from "./types/instructorId";
import type { UserId } from "./types/userId";
import { AssignmentForm } from "./components/AssignmentForm/AssignmentForm";
import { InstructorView } from "./components/InstructorView/InstructorView";
import {
  calculateCalories,
  formatDuration,
  calculatePace,
  findLongestExercise,
  findHighestCalorieExercise,
  calculateCaloriePercentage,
  calculateWeeklyLoad,
  getRestRecommendation,
} from "./utils/fitness";
import { RoutineForm } from "./components/RoutineForm/RoutineForm";
import type { User } from "./types/user";
import { ExerciseCatalog } from "./components/ExerciseCatalog/ExerciseCatalog";
import "./App.css";

function App() {
  const [exercises, setExercises] = useState<Exercise[]>([]);
  const [users, setUsers] = useState<User[]>([]);
  const [selectedUserId, setSelectedUserId] = useState<User["id"] | null>(null);
  const selectedUser = users.find((user) => user.id === selectedUserId) || null;
  const [instructors, setInstructors] = useState<Instructor[]>([]);
  const [profileType, setProfileType] = useState<"user" | "instructor">("user");
  const handleUserSubmit = (data: UserFormData) => {
    const newUserId = users.length + 1;
    setUsers((currentUsers) => [
      ...currentUsers,
      {
        id: newUserId,
        name: data.name,
        age: data.age,
        email: data.email,
        experienceLevel: data.experienceLevel,
        membershipPlan: data.membershipPlan,
        startDate: data.startDate,
        isActive: data.isActive,
      },
    ]);
    setSelectedUserId(newUserId);
  };
  const handleInstructorSubmit = (data: InstructorFormData) => {
    const newInstructorId = instructors.length + 1;
    setInstructors((currentInstructors) => [
      ...currentInstructors,
      {
        id: newInstructorId,
        name: data.name,
        age: data.age,
        email: data.email,
        assignedUsers: [],
      },
    ]);
  };
  const handleExerciseSubmit = (data: NewExercise) => {
    const nextId =
      exercises.length === 0
        ? 1
        : Math.max(...exercises.map((exercise) => exercise.id)) + 1;

    const newExercise: Exercise = {
      ...data,
      id: nextId,
    };

    setExercises((currentExercises) => [...currentExercises, newExercise]);
  };
  const handleRoutineCreate = (newRoutine: WeeklyRoutine) => {
    if (selectedUserId === null) {
      return;
    }

    setUsers((currentUsers) =>
      currentUsers.map((user) =>
        user.id === selectedUserId ? { ...user, routine: newRoutine } : user,
      ),
    );
  };
  const handleUpdateSessionComment = (day: DayOfWeek, comment: string) => {
    if (selectedUserId === null) {
      return;
    }
    setUsers((currentUsers) =>
      currentUsers.map((user) => {
        if (user.id !== selectedUserId || !user.routine) {
          return user;
        }
        return {
          ...user,
          routine: {
            ...user.routine,
            sessions: user.routine.sessions.map((session) => {
              if (session.day !== day) {
                return session;
              }
              return {
                ...session,
                comment: comment,
              };
            }),
          },
        };
      }),
    );
  };
  const handleToggleExercise = (
    day: DayOfWeek,
    exerciseId: RoutineExercise["id"],
  ) => {
    if (selectedUserId === null) {
      return;
    }

    setUsers((currentUsers) =>
      currentUsers.map((user) => {
        if (user.id !== selectedUserId || !user.routine) {
          return user;
        }

        return {
          ...user,
          routine: {
            ...user.routine,
            sessions: user.routine.sessions.map((session) => {
              if (session.day !== day) {
                return session;
              }

              return {
                ...session,
                exercises: session.exercises.map((exercise) =>
                  exercise.id === exerciseId
                    ? {
                        ...exercise,
                        isCompleted: !exercise.isCompleted,
                      }
                    : exercise,
                ),
              };
            }),
          },
        };
      }),
    );
  };
  const handleAssignUser = (instructorId: InstructorId, userId: UserId) => {
    const userExists = users.some((user) => user.id === userId);

    if (!userExists) {
      return;
    }

    setInstructors((currentInstructors) => {
      const instructorExists = currentInstructors.some(
        (instructor) => instructor.id === instructorId,
      );

      const alreadyAssigned = currentInstructors.some((instructor) =>
        instructor.assignedUsers.includes(userId),
      );

      if (!instructorExists || alreadyAssigned) {
        return currentInstructors;
      }

      return currentInstructors.map((instructor) =>
        instructor.id === instructorId
          ? {
              ...instructor,
              assignedUsers: [...instructor.assignedUsers, userId],
            }
          : instructor,
      );
    });
  };
  const longestExercise = findLongestExercise(exercises);
  const highestCalorieExercise = findHighestCalorieExercise(exercises);
  const totalCalories = exercises.reduce(
    (total, exercise) => total + calculateCalories(exercise),
    0,
  );
  const weeklyLoad = selectedUser?.routine
    ? calculateWeeklyLoad(selectedUser.routine)
    : null;
  const restRecommendation = weeklyLoad
    ? getRestRecommendation(weeklyLoad)
    : null;
  return (
    <>
      <header className="app-header">
        <div className="app-header-content">
          <h1>FitTracker</h1>
          <p>Seguimiento de entrenamiento y progreso físico</p>
        </div>
      </header>

      <main className="App">
        <section className="forms-container">
          <div className="column-heading">
            <span className="section-label">GESTIÓN GENERAL</span>
            <h2>Administración</h2>
          </div>

          <section className="card">
            <h2>Registro de perfiles</h2>

            <label htmlFor="profileType">Tipo de perfil:</label>
            <select
              id="profileType"
              value={profileType}
              onChange={(e) =>
                setProfileType(e.target.value as "user" | "instructor")
              }
            >
              <option value="user">Usuario</option>
              <option value="instructor">Instructor</option>
            </select>

            {profileType === "user" ? (
              <UserForm onSubmit={handleUserSubmit} />
            ) : (
              <InstructorForm onSubmit={handleInstructorSubmit} />
            )}
          </section>

          <section className="card">
            <h2>Asignación de usuarios</h2>
            <AssignmentForm
              instructors={instructors}
              users={users}
              onAssignUser={handleAssignUser}
            />
          </section>

          <section className="card">
            <h2>Instructores y usuarios asignados</h2>
            <InstructorView instructors={instructors} users={users} />
          </section>

          <section className="card">
            <h2>Registrar ejercicio</h2>
            <ExerciseForm onSubmit={handleExerciseSubmit} />
          </section>

          <section className="card">
            <h2>Ejercicios registrados</h2>

            {exercises.length === 0 ? (
              <p>Aún no hay ejercicios registrados.</p>
            ) : (
              exercises.map((exercise) => {
                const pace = calculatePace(exercise);

                return (
                  <p key={exercise.id}>
                    {exercise.name} - {formatDuration(exercise.duration)} -{" "}
                    {calculateCalories(exercise)} cal
                    {pace !== null ? ` - Pace: ${pace} min/km` : ""}
                  </p>
                );
              })
            )}

            <p>Total de calorías: {totalCalories}</p>
          </section>

          <section className="card">
            <ExerciseCatalog exercises={exercises} />
          </section>

          <section className="card">
            <h2>Resumen comparativo</h2>

            {longestExercise && (
              <p>
                Mayor duración: {longestExercise.name} (
                {longestExercise.duration} min)
              </p>
            )}

            {highestCalorieExercise && (
              <p>
                Más calorías: {highestCalorieExercise.name} (
                {calculateCalories(highestCalorieExercise)} cal,{" "}
                {calculateCaloriePercentage(
                  highestCalorieExercise,
                  totalCalories,
                )}
                % del total)
              </p>
            )}

            <h3>Contribución al total de calorías:</h3>

            {exercises.map((exercise) => (
              <p key={exercise.id}>
                {exercise.name} ({calculateCalories(exercise)} cal,{" "}
                {calculateCaloriePercentage(exercise, totalCalories)}% del
                total)
              </p>
            ))}
          </section>
        </section>

        <section className="results-container">
          <div className="column-heading">
            <span className="section-label">CONTROL Y PROGRESO</span>
            <h2>Seguimiento de usuarios</h2>
          </div>

          <section className="card">
            <h2>Seleccionar usuario</h2>

            <select
              value={selectedUserId ?? ""}
              onChange={(event) => {
                setSelectedUserId(
                  event.target.value === "" ? null : Number(event.target.value),
                );
              }}
            >
              <option value="">Seleccione un usuario</option>

              {users.map((user) => (
                <option key={user.id} value={user.id}>
                  {user.name}
                </option>
              ))}
            </select>

            {!selectedUser && (
              <p>Seleccione un usuario para consultar o gestionar su rutina.</p>
            )}
          </section>

          {selectedUser && (
            <section className="card">
              <h2>Perfil del usuario</h2>
              <p>Nombre: {selectedUser.name}</p>
              <p>Edad: {selectedUser.age}</p>
              <p>Nivel: {selectedUser.experienceLevel}</p>
              <p>Membresía: {selectedUser.membershipPlan}</p>
              <p>
                Fecha de inicio:{" "}
                {selectedUser.startDate.toLocaleDateString("es-CR")}
              </p>
              <p>
                Membresía activa:{" "}
                {selectedUser.isActive ? "Activa" : "Inactiva"}
              </p>
            </section>
          )}

          {selectedUser && (
            <>
              {selectedUser.routine && (
                <p className="routine-warning">
                  Este usuario ya tiene una rutina asignada. Si creas una nueva,
                  reemplazará la anterior.
                </p>
              )}

              <RoutineForm
                key={selectedUser.id}
                exercises={exercises}
                onCreateRoutine={handleRoutineCreate}
              />
            </>
          )}

          {selectedUser?.routine && (
            <RoutineView
              routine={selectedUser.routine}
              onToggleExercise={handleToggleExercise}
              onUpdateSessionComment={handleUpdateSessionComment}
            />
          )}

          {weeklyLoad && restRecommendation && (
            <WeeklyLoadView
              weeklyLoad={weeklyLoad}
              restRecommendation={restRecommendation}
            />
          )}
        </section>
      </main>
    </>
  );
}

export default App;
