import { UserForm } from "../../fit-tracker/src/components/UserForm/UserForm";
import type { UserFormData } from "./components/UserForm/UserForm";
import { useState } from "react";
import { ExerciseForm } from "./components/ExerciseForm/ExerciseForm";
import type { ExerciseFormData } from "./components/ExerciseForm/ExerciseForm";
import "./App.css";

function App() {
  const [profile, setProfile] = useState<UserFormData | null>(null);
  const [exercises, setExercises] = useState<ExerciseFormData[]>([]);
  const handleUserSubmit = (data: UserFormData) => {
    setProfile(data);
  };
  const handleExerciseSubmit = (data: ExerciseFormData) => {
    setExercises((currentExercises) => [...currentExercises, data]);
  };
  return (
    <div className="App">
      <UserForm onSubmit={handleUserSubmit} />
      {profile && (
        <section>
          {profile.name} {profile.age} {profile.experienceLevel}
        </section>
      )}
      <ExerciseForm onSubmit={handleExerciseSubmit} />
      <section>
        {exercises.map((exercise, index) => (
          <p key={index}>{exercise.name} </p>
        ))}
      </section>
    </div>
  );
}

export default App;
