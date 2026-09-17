import type { Exercise } from "../types/exercise";

const running: Exercise = {
  name: "Running",
  duration: 30,
  caloriesPerMinute: 10,
  distance: 5,
};

const cycling: Exercise = {
  name: "Cycling",
  duration: 45,
  caloriesPerMinute: 8,
};

const exercises: Exercise[] = [running, cycling];

export default exercises;
