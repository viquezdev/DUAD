type MembershipPlan = "Basic" | "Premium" | "VIP";

export interface Membership {
  membershipPlan: MembershipPlan;
  startDate: Date;
  isActive: boolean;
}
