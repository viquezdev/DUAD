import type { RoutineExercise } from "./routineExercise";
import type { DayOfWeek } from "./routineEntry";

export interface DaySession {
  day: DayOfWeek;
  exercises: RoutineExercise[];
  comment?: string;
}
