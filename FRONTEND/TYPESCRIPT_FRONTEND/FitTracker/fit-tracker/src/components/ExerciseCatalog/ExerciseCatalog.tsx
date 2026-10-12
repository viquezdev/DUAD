import type { Exercise } from "../../types/exercise";

interface ExerciseCatalogProps {
  exercises: Exercise[];
}

export const ExerciseCatalog = ({ exercises }: ExerciseCatalogProps) => {
  return <div>ExerciseCatalog</div>;
};

export default ExerciseCatalog;
