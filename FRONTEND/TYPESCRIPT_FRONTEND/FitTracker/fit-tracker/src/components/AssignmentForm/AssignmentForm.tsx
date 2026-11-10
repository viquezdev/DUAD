import type { Instructor } from "../../types/instructor";
import type { User } from "../../types/user";
import { useState } from "react";
import "./AssignmentForm.css";

type AssignmentFormProps = {
  instructors: Instructor[];
  users: User[];
  onAssignUser: (instructorId: number, userId: number) => void;
};

export function AssignmentForm({
  instructors,
  users,
  onAssignUser,
}: AssignmentFormProps) {
  const [selectedInstructorId, setSelectedInstructorId] = useState<number>(0);
  const [selectedUserId, setSelectedUserId] = useState<number>(0);
  const availableUsers = users.filter(
    (user) =>
      !instructors.some((instructor) =>
        instructor.assignedUsers.includes(user.id),
      ),
  );
  return (
    <div className="assignment-form">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          if (!selectedInstructorId || !selectedUserId) {
            return;
          }
          onAssignUser(selectedInstructorId, selectedUserId);
          setSelectedInstructorId(0);
          setSelectedUserId(0);
        }}
      >
        <h2>Asignar usuario a instructor</h2>
        <label htmlFor="instructor">Seleccionar instructor:</label>

        <select
          id="instructor"
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

        <label htmlFor="usuario">Seleccionar usuario:</label>

        <select
          id="usuario"
          value={selectedUserId}
          onChange={(e) => setSelectedUserId(Number(e.target.value))}
        >
          <option value={0}>Seleccione un usuario</option>

          {availableUsers.map((user) => (
            <option key={user.id} value={user.id}>
              {user.name}
            </option>
          ))}
        </select>

        <button type="submit">Asignar usuario</button>
      </form>
    </div>
  );
}
