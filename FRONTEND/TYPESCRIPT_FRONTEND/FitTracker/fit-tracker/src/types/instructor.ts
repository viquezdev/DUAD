import type { Person } from "./person";
import type { UserId } from "./userId";
import type { InstructorId } from "./instructorId";
export interface Instructor extends Person {
  id: InstructorId;
  assignedUsers: UserId[];
}
