import type { ExperienceLevel } from "./experienceLevel";
import type { WeeklyRoutine } from "./weeklyRoutine";

export interface User {
  name: string;
  age: number;
  experienceLevel: ExperienceLevel;
  routine: WeeklyRoutine;
}
