import type { WeeklyRoutine } from "../types/weeklyRoutine";
import exercises from "./exercises";

const strengthRoutine: WeeklyRoutine = {
  name: "Strength Training",
  entries: [
    { day: "Monday", exercise: exercises[0] },
    { day: "Wednesday", exercise: exercises[1] },
  ],
};

export default strengthRoutine;
