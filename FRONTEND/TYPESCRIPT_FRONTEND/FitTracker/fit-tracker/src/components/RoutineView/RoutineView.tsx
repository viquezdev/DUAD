import type { WeeklyRoutine } from "../../types/weeklyRoutine";
import type { DayOfWeek } from "../../types/routineEntry";
import type { RoutineExercise } from "../../types/routineExercise";

type RoutineViewProps = {
  routine: WeeklyRoutine;
  onToggleExercise: (day: DayOfWeek, exerciseId: RoutineExercise["id"]) => void;
};
