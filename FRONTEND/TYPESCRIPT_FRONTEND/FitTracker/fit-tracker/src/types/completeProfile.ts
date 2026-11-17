import type { PersonalData } from "./personalData";
import type { Membership } from "./membership";

export interface CompleteProfile extends PersonalData, Membership {}
