import { UserForm } from "../../fit-tracker/src/components/UserForm/UserForm";
import type { UserFormData } from "./components/UserForm/UserForm";
import { useState } from "react";
import { ExerciseForm } from "./components/ExerciseForm/ExerciseForm";
import type { ExerciseFormData } from "./components/ExerciseForm/ExerciseForm";
import type { WeeklyRoutine } from "./types/weeklyRoutine";
import {
  calculateCalories,
  formatDuration,
  calculatePace,
  findLongestExercise,
  findHighestCalorieExercise,
  calculateCaloriePercentage,
  calculateAverageCalories,
  calculateRoutineCalories,
  findHighestCalorieDay,
} from "./utils/fitness";
import { RoutineForm } from "./components/RoutineForm/RoutineForm";
import type { User } from "./types/user";
import "./App.css";

function App() {
  const [profile, setProfile] = useState<UserFormData | null>(null);
  const [user, setUser] = useState<User | null>(null);
  const [exercises, setExercises] = useState<ExerciseFormData[]>([]);
  const [routine, setRoutine] = useState<WeeklyRoutine | null>(null);
  const handleUserSubmit = (data: UserFormData) => {
    setProfile(data);
  };
  const handleExerciseSubmit = (data: ExerciseFormData) => {
    setExercises((currentExercises) => [...currentExercises, data]);
  };
  const handleRoutineCreate = (newRoutine: WeeklyRoutine) => {
    setRoutine(newRoutine);
    if (!profile) {
      return;
    }

    const newUser: User = {
      name: profile.name,
      age: profile.age,
      experienceLevel: profile.experienceLevel,
      routine: newRoutine,
    };
    setUser(newUser);
  };
  const longestExercise = findLongestExercise(exercises);
  const highestCalorieExercise = findHighestCalorieExercise(exercises);
  const totalCalories = exercises.reduce(
    (total, exercise) => total + calculateCalories(exercise),
    0,
  );
  const highestCalorieDay = routine ? findHighestCalorieDay(routine) : null;
  return (
    <>
      <header className="app-header">
        <h1>FitTracker</h1>
        <p>Seguimiento de tu entrenamiento</p>
      </header>
      <div className="App">
        <div className="forms-container">
          <UserForm onSubmit={handleUserSubmit} />

          <ExerciseForm onSubmit={handleExerciseSubmit} />
          <RoutineForm
            exercises={exercises}
            onCreateRoutine={handleRoutineCreate}
          />
        </div>
        <div className="results-container">
          {profile && (
            <section className="card">
              <h2>Perfil de Usuario</h2>
              <p>Nombre: {profile.name}</p>
              <p>Edad: {profile.age}</p>
              <p>Nivel: {profile.experienceLevel}</p>
            </section>
          )}
          {user && (
            <section className="card">
              <h2>Rutina asignada</h2>
              <p>Nombre: {user.name}</p>
              <p>Edad: {user.age}</p>
              <p>Nivel: {user.experienceLevel}</p>
              <p>Rutina: {user.routine.name}</p>
              <h3>Entrenamientos</h3>
              {user.routine.entries.map((entry, index) => (
                <p key={index}>
                  {entry.day} → {entry.exercise.name}
                </p>
              ))}
            </section>
          )}
          {routine && (
            <section className="card">
              <h2>Rutina creada</h2>

              <h3>{routine.name}</h3>

              {routine.entries.map((entry, index) => (
                <p key={index}>
                  {entry.day} → {entry.exercise.name}
                </p>
              ))}
              <p>Calorías totales: {calculateRoutineCalories(routine)}</p>
              <p>
                Promedio de calorías por día:{" "}
                {calculateAverageCalories(routine)}
              </p>
              <p>Día con más calorías: {highestCalorieDay}</p>
            </section>
          )}

          <section className="card">
            <h2>Ejercicios registrados</h2>
            {exercises.map((exercise, index) => (
              <p key={index}>
                {exercise.name} - {formatDuration(exercise.duration)} -{" "}
                {calculateCalories(exercise)} -
                {calculatePace(exercise) !== null
                  ? `Pace: ${calculatePace(exercise)} min/km`
                  : ""}
              </p>
            ))}
            <p>Total de calorías: {totalCalories}</p>
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
                Más calorías : {highestCalorieExercise.name} (
                {calculateCalories(highestCalorieExercise)} cal,{" "}
                {calculateCaloriePercentage(
                  highestCalorieExercise,
                  totalCalories,
                )}
                % del total)
              </p>
            )}
          </section>
        </div>
      </div>
    </>
  );
}

export default App;
