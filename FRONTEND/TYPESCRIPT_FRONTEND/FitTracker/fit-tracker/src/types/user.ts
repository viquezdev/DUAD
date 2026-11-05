import type { WeeklyRoutine } from "./weeklyRoutine";
import type { UserId } from "./userId";
import type { CompleteProfile } from "./completeProfile";

export interface User extends CompleteProfile {
  id: UserId;
  routine: WeeklyRoutine;
}
