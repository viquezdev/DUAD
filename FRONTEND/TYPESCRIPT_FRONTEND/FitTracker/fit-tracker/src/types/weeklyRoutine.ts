import type { RoutineId } from "./routineId";
import type { DaySession } from "./daySession";

export interface WeeklyRoutine {
  id: RoutineId;
  name: string;
  startDate: Date;
  sessions: DaySession[];
}
