import type { Category } from "./category";
import type { Exercise } from "./exercise";

export interface CategorySummary {
  category: Category;
  exercises: Exercise[];
  totalMinutes: number;
  totalCalories: number;
}
