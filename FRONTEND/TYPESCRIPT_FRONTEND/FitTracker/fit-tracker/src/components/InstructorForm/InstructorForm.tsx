import { useState } from "react";
import type { Instructor } from "../../types/instructor";

import "./InstructorForm.css";

export function InstructorForm({ onSubmit }: InstructorFormProps) {
  const [name, setName] = useState<string>("");
  const [age, setAge] = useState<number>(0);
  const [email, setEmail] = useState<string>("");
  return (
    <div className="instructor-form">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          if (!name.trim() || age <= 0 || !email.trim()) {
            return;
          }
          onSubmit({
            name,
            age,
            email,
          });
          setName("");
          setAge(0);
          setEmail("");
        }}
      >
        <h2>Registro de perfil de instructor</h2>
        <label htmlFor="instructor-name">Name:</label>
        <input
          type="text"
          id="instructor-name"
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
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <button type="submit">Registrar perfil</button>
      </form>
    </div>
  );
}

export type InstructorFormData = Pick<Instructor, "name" | "age" | "email">;

type InstructorFormProps = {
  onSubmit: (data: InstructorFormData) => void;
};

export default InstructorForm;
