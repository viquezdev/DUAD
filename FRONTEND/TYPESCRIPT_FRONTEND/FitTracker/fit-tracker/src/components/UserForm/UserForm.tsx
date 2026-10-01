import { useState } from "react";
import type { ExperienceLevel } from "../../types/experienceLevel";
import type { User } from "../../types/user";
import "./UserForm.css";
export function UserForm({ onSubmit }: UserFormProps) {
  const [name, setName] = useState<string>("");
  const [age, setAge] = useState<number>(0);
  const [experienceLevel, setExperienceLevel] =
    useState<ExperienceLevel>("beginner");
  return (
    <div className="user-form">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit({ name, age, experienceLevel });
          setName("");
          setAge(0);
          setExperienceLevel("beginner");
        }}
      >
        <h2>Registro de perfil</h2>
        <label htmlFor="user-name">Name:</label>
        <input
          type="text"
          id="user-name"
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
          onChange={(e) =>
            setExperienceLevel(e.target.value as ExperienceLevel)
          }
        >
          <option value="beginner">Beginner</option>
          <option value="intermediate">Intermediate</option>
          <option value="advanced">Advanced</option>
        </select>
        <button type="submit">Registrar perfil</button>
      </form>
    </div>
  );
}

export type UserFormData = Pick<User, "name" | "age" | "experienceLevel">;

type UserFormProps = {
  onSubmit: (data: UserFormData) => void;
};

export default UserForm;
