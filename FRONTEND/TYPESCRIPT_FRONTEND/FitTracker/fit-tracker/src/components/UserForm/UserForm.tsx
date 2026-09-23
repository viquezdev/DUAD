import { useState } from "react";
import type { ExperienceLevel } from "../../types/experienceLevel";

export function UserForm({ onSubmit }: UserFormProps) {
  const [name, setName] = useState<string>("");
  const [age, setAge] = useState<number>(0);
  const [experienceLevel, setExperienceLevel] =
    useState<ExperienceLevel>("beginner");
  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit({ name, age, experienceLevel });
      }}
    >
      <label htmlFor="name">Name:</label>
      <input
        type="text"
        id="name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <label htmlFor="age">Age:</label>
      <input
        type="number"
        id="age"
        value={age}
        onChange={(e) => setAge(Number(e.target.value))}
      />
      <label htmlFor="experienceLevel">Experience Level:</label>
      <select
        id="experienceLevel"
        value={experienceLevel}
        onChange={(e) => setExperienceLevel(e.target.value as ExperienceLevel)}
      >
        <option value="beginner">Beginner</option>
        <option value="intermediate">Intermediate</option>
        <option value="advanced">Advanced</option>
      </select>
      <button type="submit">Registrar perfil</button>
    </form>
  );
}

export type UserFormData = {
  name: string;
  age: number;
  experienceLevel: ExperienceLevel;
};

type UserFormProps = {
  onSubmit: (data: UserFormData) => void;
};

export default UserForm;
