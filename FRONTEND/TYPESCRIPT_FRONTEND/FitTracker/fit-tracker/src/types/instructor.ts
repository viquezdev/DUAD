import type { Person } from "./person";
import type { User } from "./user";
import type { InstructorId } from "./instructorId";
export interface Instructor extends Person {
  id: InstructorId;
  assignedUsers: User[];
}
