import type { CaloriesPerMinute } from "./caloriesPerMinute";
export interface Exercise {
  name: string;
  duration: number;
  caloriesPerMinute: CaloriesPerMinute;
  distance?: number;
}
