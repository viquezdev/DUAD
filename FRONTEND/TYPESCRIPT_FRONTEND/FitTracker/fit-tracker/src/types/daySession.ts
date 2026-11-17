import type { RoutineExercise } from "./routineExercise";
import type { DayOfWeek } from "./dayOfWeek";

export interface DaySession {
  day: DayOfWeek;
  exercises: RoutineExercise[];
  comment?: string;
}
