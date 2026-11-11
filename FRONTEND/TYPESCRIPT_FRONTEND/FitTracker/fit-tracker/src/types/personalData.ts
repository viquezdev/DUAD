import type { ExperienceLevel } from "./experienceLevel";
import type { Person } from "./person";

export interface PersonalData extends Person {
  experienceLevel: ExperienceLevel;
}
