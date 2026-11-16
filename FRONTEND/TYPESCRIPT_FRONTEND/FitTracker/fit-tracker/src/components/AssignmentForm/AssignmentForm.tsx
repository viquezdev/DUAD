import type { Instructor } from "../../types/instructor";
import type { User } from "../../types/user";
import { useState } from "react";
import type { InstructorId } from "../../types/instructorId";
import type { UserId } from "../../types/userId";
import "./AssignmentForm.css";

interface AssignmentFormProps {
  instructors: Instructor[];
  users: User[];
  onAssignUser: (instructorId: InstructorId, userId: UserId) => void;
}

export function AssignmentForm({
  instructors,
  users,
  onAssignUser,
}: AssignmentFormProps) {
  const [selectedInstructorId, setSelectedInstructorId] =
    useState<InstructorId | null>(null);
  const [selectedUserId, setSelectedUserId] = useState<UserId | null>(null);
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
          setSelectedInstructorId(null);
          setSelectedUserId(null);
        }}
      >
        <h2>Asignar usuario a instructor</h2>
        <label htmlFor="instructor">Seleccionar instructor:</label>

        <select
          id="instructor"
          value={selectedInstructorId ?? ""}
          onChange={(e) =>
            setSelectedInstructorId(
              e.target.value === "" ? null : Number(e.target.value),
            )
          }
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
          value={selectedUserId ?? ""}
          onChange={(e) =>
            setSelectedUserId(
              e.target.value === "" ? null : Number(e.target.value),
            )
          }
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
