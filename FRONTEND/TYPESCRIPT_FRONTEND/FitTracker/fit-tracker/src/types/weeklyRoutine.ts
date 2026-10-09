import type { RoutineEntry } from "./routineEntry";
import type { RoutineId } from "./routineId";

export interface WeeklyRoutine {
  id: RoutineId;
  name: string;
  entries: RoutineEntry[];
}
