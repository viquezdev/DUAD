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
} from "./utils/fitness";
import { RoutineForm } from "./components/RoutineForm/RoutineForm";
import "./App.css";

function App() {
  const [profile, setProfile] = useState<UserFormData | null>(null);
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
  };
  const longestExercise = findLongestExercise(exercises);
  const highestCalorieExercise = findHighestCalorieExercise(exercises);
  const totalCalories = exercises.reduce(
    (total, exercise) => total + calculateCalories(exercise),
    0,
  );
  return (
    <div className="App">
      <UserForm onSubmit={handleUserSubmit} />
      {profile && (
        <section>
          {profile.name} {profile.age} {profile.experienceLevel}
        </section>
      )}
      <ExerciseForm onSubmit={handleExerciseSubmit} />
      <RoutineForm
        exercises={exercises}
        onCreateRoutine={handleRoutineCreate}
      />
      {routine && (
        <section>
          <h2>Rutina creada</h2>

          <h3>{routine.name}</h3>

          {routine.entries.map((entry, index) => (
            <p key={index}>
              {entry.day} → {entry.exercise.name}
            </p>
          ))}
          <p>Calorías totales: {calculateRoutineCalories(routine)}</p>
          <p>
            Promedio de calorías por día: {calculateAverageCalories(routine)}
          </p>
        </section>
      )}
      <section>
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

        <section>
          <h2>Resumen comparativo</h2>

          {longestExercise && (
            <p>
              Mayor duración: {longestExercise.name} ({longestExercise.duration}{" "}
              min)
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
              % del total))
            </p>
          )}
        </section>
      </section>
    </div>
  );
}

export default App;
