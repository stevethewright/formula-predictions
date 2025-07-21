export interface Event {
  roundNumber: number;
  country: string;
  location: string;
  officialEventName: string;
  eventName: string;
  eventDate: string;
  eventFormat: string;
  session1: string;
  session1Date: string;
  session1DateUtc: string;
  session2: string;
  session2Date: string;
  session2DateUtc: string;
  session3: string;
  session3Date: string;
  session3DateUtc: string;
  session4: string;
  session4Date: string;
  session4DateUtc: string;
  session5: string;
  session5Date: string;
  session5DateUtc: string;
  f1ApiSupport: boolean;
}
