import { useState } from "react";
import type { ExperienceLevel } from "../../types/experienceLevel";
import type { User } from "../../types/user";
import type { MembershipPlan } from "../../types/membership";

import "./UserForm.css";
export function UserForm({ onSubmit }: UserFormProps) {
  const [name, setName] = useState<string>("");
  const [age, setAge] = useState<number>(0);
  const [experienceLevel, setExperienceLevel] =
    useState<ExperienceLevel>("beginner");
  const [membershipPlan, setMembershipPlan] = useState<MembershipPlan>("Basic");
  const [startDate, setStartDate] = useState<string>("");
  const [isActive, setIsActive] = useState<boolean>(true);
  return (
    <div className="user-form">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          if (!name.trim() || age <= 0 || !startDate) {
            return;
          }
          onSubmit({
            name,
            age,
            experienceLevel,
            membershipPlan,
            startDate: new Date(startDate),
            isActive,
          });
          setName("");
          setAge(0);
          setExperienceLevel("beginner");
          setMembershipPlan("Basic");
          setStartDate("");
          setIsActive(true);
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
        <label htmlFor="membershipPlan">Membresía:</label>
        <select
          id="membershipPlan"
          value={membershipPlan}
          onChange={(e) => setMembershipPlan(e.target.value as MembershipPlan)}
        >
          <option value="Basic">Basic</option>
          <option value="Premium">Premium</option>
          <option value="VIP">VIP</option>
        </select>

        <label htmlFor="startDate">Fecha:</label>
        <input
          type="date"
          id="startDate"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
        />

        <label htmlFor="isActive">Activo:</label>
        <input
          type="checkbox"
          id="isActive"
          checked={isActive}
          onChange={(e) => setIsActive(e.target.checked)}
        />

        <button type="submit">Registrar perfil</button>
      </form>
    </div>
  );
}

export type UserFormData = Pick<
  User,
  | "name"
  | "age"
  | "experienceLevel"
  | "membershipPlan"
  | "startDate"
  | "isActive"
>;

type UserFormProps = {
  onSubmit: (data: UserFormData) => void;
};

export default UserForm;
