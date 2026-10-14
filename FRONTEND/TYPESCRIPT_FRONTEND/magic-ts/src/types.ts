// Define los colores válidos de las cartas
export type MagicColor = "White" | "Blue" | "Black" | "Red" | "Green";

// Define la rareza de las cartas
export type Rarity = "Common" | "Uncommon" | "Rare" | "Mythic Rare";

// Define la estructura de una carta de Magic
export interface MagicCard {
  id: string;
  name: string;
  manaCost?: string;
  cmc?: number;
  colors?: MagicColor[];
  type: string;
  rarity: Rarity;
  set: string;
  text?: string;
  power?: string;
  toughness?: string;
  imageUrl?: string;
}

// Interfaz base para todas las respuestas de la API
export interface BaseApiResponse {
  status: number;
  [key: string]: unknown;
}

// Define una estructura genérica para las respuestas de la API
export interface ApiResponse<T> extends BaseApiResponse {
  cards: T[];
}
