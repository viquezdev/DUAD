import type { ExperienceLevel } from "./experienceLevel";
import type { WeeklyRoutine } from "./weeklyRoutine";
import type { UserId } from "./userId";

export interface User {
  id: UserId;
  name: string;
  age: number;
  experienceLevel: ExperienceLevel;
  routine: WeeklyRoutine;
}
