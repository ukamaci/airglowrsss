/***************************************************************************
                          schedule.cpp  -  description
                             -------------------
    begin                : Wed Aug 6 2003
    copyright            : (C) 2003 by Jonathan Makela
    email                : jmakela@nrl.navy.mil
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#include "schedule.h"
#include "system.h"

extern System mySystem;

Schedule::Schedule(){
  myMoonAngle = 0.;
  mySunAngle = 18.;
  myMoonSet = true;
  myScheduleMode = SCHEDULE_OFF;
  myLatitude = myLongitude = 0.0;
}
Schedule::~Schedule(){
}
/** Set the moon angle above horizon */
void Schedule::SetMoonAngle(double angle){
  // do error checking and set to a safe answer if out of bounds
  if(angle < -90 || angle > 90)
  {
    char str[64];
    sprintf(str, "Bad moon angle given: %5.3f (Schedule::SetMoonAngle)", angle);
    mySystem.myConfiguration.myLogger.WriteErrorString(str);
    angle = 0.;
  }

  myMoonAngle = angle;

  // If the mode is set to Auto, automatically set the start and stop times
  if(myScheduleMode == SCHEDULE_AUTO)
    AutoSetTimes();
}

/** Returns the scheduler's latitude */
float Schedule::GetLatitude(){
  return myLatitude;
}
/** Returns the schedulers's longitude */
float Schedule::GetLongitude(){
  return myLongitude;
}


/** Set the sun angle above horizon */
void Schedule::SetSunAngle(double angle){
  // do error checking and set to a safe answer if out of bounds
  if(angle < -90 || angle > 90)
  {
    char str[64];
    sprintf(str, "Bad moon angle given: %5.3f (Schedule::SetMoonAngle)", angle);
    mySystem.myConfiguration.myLogger.WriteErrorString(str);
    angle = -18.0;
  }

  mySunAngle = angle;

  // If the mode is set to Auto, automatically set the start and stop times
  if(myScheduleMode == SCHEDULE_AUTO)
    AutoSetTimes();
}
/** Copy constructor */
Schedule::Schedule(const Schedule& s){
   myMoonAngle = s.myMoonAngle;
   myMoonSet = s.myMoonSet;
   myScheduleMode = s.myScheduleMode;
   myStartTime = s.myStartTime;
   myStopTime = s.myStopTime;
   mySunAngle = s.mySunAngle;
}
/** Write the schedule class to config file */
void Schedule::Write(ofstream& os){
  // Put the header label
  os << "#Schedule" << endl;

  // Write the angles
  os << myMoonAngle << endl;
  os << mySunAngle << endl;

  // Write the flags
  os << myMoonSet << endl;
  os << myScheduleMode << endl;

  // Write the lat/lon
  os << myLatitude << endl;
  os << myLongitude << endl;
}
/** Read Schedule class from config file */
void Schedule::Read(ifstream& is){
  // Search for the header from the beginning of the file
  is.seekg(0,ios::beg);

  string myLine;

  // Read in the next line of the file
  getline(is, myLine);

  // Find the header
  while(myLine != "#Schedule" && !is.eof())
    getline(is, myLine);

  if(is.eof())
  {
    mySystem.myConfiguration.myLogger.WriteErrorString("End of configuration file reached before #Schedule found");
    return;
  }

  string str;

  // Read the angles
  is >> myMoonAngle;
  is >> mySunAngle;

  // Read the flags
  is >> myMoonSet;
  is >> myScheduleMode;

  // Read the lat/lon
  is >> myLatitude;
  is >> myLongitude;

  if(myScheduleMode == SCHEDULE_AUTO)
    AutoSetTimes();
}
/** Set the moonset flag */
void Schedule::SetMoonSet(bool flag){
  myMoonSet = flag;
  
  if(myScheduleMode == SCHEDULE_AUTO)
    AutoSetTimes();
}
/** Returns the moonset flag */
bool Schedule::GetMoonSet(){
  return myMoonSet;
}
/** Return the moonangle variable */
double Schedule::GetMoonAngle(){
  return myMoonAngle;
}
/** Returns the sun angle variable */
double Schedule::GetSunAngle(){
  return mySunAngle;
}
/** Returns the start time */
tm Schedule::GetStartTime(){
  return myStartTime;
}

/** No descriptions */
void Schedule::SetLatitude(float lat){
  if(lat < -90 || lat > 90){
    mySystem.myConfiguration.myLogger.WriteErrorString("Latitude out of range (Schedule::SetLatitude");
    lat = -999.;
  }

  myLatitude = lat;

//  if(mySystem.myConfiguration.mySchedule.GetScheduleMode() == SCHEDULE_AUTO)
//    mySystem.myConfiguration.mySchedule.AutoSetTimes();
}
/** No descriptions */
void Schedule::SetLongitude(float lon){
  // Make sure the lat/lon make sense
  while(lon < 0) {
    mySystem.myConfiguration.myLogger.WriteErrorString("Longitude out of range (Schedule::SetLongitude");
    lon = lon + 360.;
  }
  while(lon > 360) {
    mySystem.myConfiguration.myLogger.WriteErrorString("Longitude out of range (Schedule::SetLongitude");
    lon = lon - 360.;
  }

  myLongitude = lon;

//  if(mySystem.myConfiguration.mySchedule.GetScheduleMode() == SCHEDULE_AUTO)
//    mySystem.myConfiguration.mySchedule.AutoSetTimes();
}

/** Sets the start time */
void Schedule::SetStartTime(tm start){
  myStartTime = start;
}
/** Gets the stop time */
tm Schedule::GetStopTime(){
  cout << "WHAT?";
  return myStopTime;
}
/** Sets the stop time */
void Schedule::SetStopTime(tm stop){
  myStopTime = stop;
}
/** Calculates the rise and set times of the sun and moon for the given day and location. */
void Schedule::GetRiseSetTimes(int month, int day, int year, double lat,
                                double lon, int timezone, double *sunrise,
                                double *sunset, double *moonrise, double *moonset){
	// Get the rise and set time for the location
	double transittime;
	double azr,azs,altt;
	int	   status;
	Now	   np;

  // Add 1 to month because it comes from struct tm for which month is 0 based
  // Add 1900 to year because it comes from struct tm for which year is 1900 based
	mySunAndMoon.cal_mjd(month+1,(double)day+0.5,year+1900,&(np.n_mjd));
	np.n_lat =  lat * 3.1415926/180.0;
	np.n_lng = lon * 3.1415926/180.0;
	np.n_tz  = timezone;
	np.n_temp =  0;
	np.n_pressure = 1000;
	np.n_height   = 0;
	np.n_epoch    = EOD;
	np.n_tznm[0] = '?';
	np.n_tznm[1] = '?';
	np.n_tznm[2] = '?';
	np.n_tznm[3] = 0;

	status = 0;
	mySunAndMoon.riset_cir (MOON, &np, MANUAL, moonrise, moonset,&transittime, &azr, &azs, &altt, &status);
	if (status & RS_NORISE) *moonrise = MY_NORISE;
	if (status & RS_NOSET) *moonset = MY_NOSET;

	if (status & RS_ERROR) *moonrise = MY_ERROR;
	if (status & RS_CIRCUMPOLAR) {
		*moonrise = MY_UPALL;
		*moonset = MY_UPALL;
	}
	if (status & RS_NEVERUP) {
		*moonset = *moonrise = MY_DOWNALL;
	}

	status=0;
	mySunAndMoon.riset_cir (SUN, &np, MANUAL, sunrise, sunset,&transittime, &azr, &azs, &altt, &status);
	if (status & RS_NORISE) *sunrise = MY_NORISE;
	if (status & RS_NOSET) *sunset = MY_NOSET;

	if (status & RS_ERROR) *sunrise = MY_ERROR;
	if (status & RS_CIRCUMPOLAR) {
		*sunrise = MY_UPALL;
		*sunset = MY_UPALL;
	}
	if (status & RS_NEVERUP) {
    *sunset = *sunrise = MY_DOWNALL;
  }

  // Need to subtract 1 to make it 0 based
  // MAY NOT BE RIGHT!!!
//  *sunrise -= 1.;
//  *sunset -= 1.;
//  *moonrise -= 1.;
//  *moonset -= 1.;

}
/** Returns whether the current time is between rise and set or not */
int Schedule::isUp(double time, double rise, double set){
  // check to see if the body is up at the current time
  if(rise > set)
    return !(time>set && time<rise);
  else
    return (time>rise && time<set);
}
/** Sets the start and stop time based upon the current scheduling configuration and the sun and moon rise/set times. */
bool Schedule::AutoSetTimes(){
// Automatically set the start and stop time based on
// the current location and current time

  time_t UT_time, LT_time;
  UT_time = time(NULL);
  LT_time = time(NULL);

  struct tm LT;
  struct tm UT;

  // Get the current LT and UT
  UT = *gmtime(&UT_time);
  LT = *localtime(&LT_time);
    
  struct tm start = LT;
  struct tm stop = LT;
  struct tm temp_tm;

  double sunrise, sunset, moonrise, moonset;
  double nextsunrise, nextsunset, nextmoonrise, nextmoonset;

  int extra_day = 0;
  bool fullmoon = true;

//  if(LT.tm_hour < 12)
//  {
//    // We are before noon local so use yesterday
//    extra_day = -1;
//  }
  
  int GMTHour = UT.tm_hour;
  int LTHour = LT.tm_hour;
  int TimeZone = ((GMTHour - LTHour) + 24) % 24;

  mySunAndMoon.m_MoonAngle = DegRad(myMoonAngle);
  mySunAndMoon.m_SunAngle = DegRad(mySunAngle);

  if(myMoonSet)
  {
    // Yes, we do.  Find when it rises and sets
    while(fullmoon)
    {
      // Get the rise and set times for the sun and the moon for today
      GetRiseSetTimes(LT.tm_mon, LT.tm_mday + extra_day, LT.tm_year,
                      myLatitude, myLongitude,
//                      mySystem.myConfiguration.mySite.GetLatitude(),
//                      mySystem.myConfiguration.mySite.GetLongitude(),
                      TimeZone, &sunrise, &sunset, &moonrise, &moonset);

      // Set the sunrise and sunset times
      mySunRiseTime.tm_hour = (int) sunrise;
      mySunRiseTime.tm_min = (int) (sunrise*60. - mySunRiseTime.tm_hour*60.);
      mySunRiseTime.tm_sec = (int) (sunrise*3600. - mySunRiseTime.tm_min*60. - mySunRiseTime.tm_hour*3600.);
      mySunSetTime.tm_hour = (int) sunset;
      mySunSetTime.tm_min = (int) (sunset*60. - mySunSetTime.tm_hour*60.);
      mySunSetTime.tm_sec = (int) (sunset*3600. - mySunSetTime.tm_min*60. - mySunSetTime.tm_hour*3600.);
      myMoonRiseTime.tm_hour = (int) moonrise;
      myMoonRiseTime.tm_min = (int) (moonrise*60. - myMoonRiseTime.tm_hour*60.);
      myMoonRiseTime.tm_sec = (int) (moonrise*3600. - myMoonRiseTime.tm_min*60. - myMoonRiseTime.tm_hour*3600.);
      myMoonSetTime.tm_hour = (int) moonset;
      myMoonSetTime.tm_min = (int) (moonset*60. - myMoonSetTime.tm_hour*60.);
      myMoonSetTime.tm_sec = (int) (moonset*3600. - myMoonSetTime.tm_min*60. - myMoonSetTime.tm_hour*3600.);
        
      // Get the rise and set times for the sun and the moon for tomorrow
      GetRiseSetTimes(LT.tm_mon, LT.tm_mday + 1 + extra_day, LT.tm_year,
		      myLatitude, myLongitude,
//                      mySystem.myConfiguration.mySite.GetLatitude(),
//                      mySystem.myConfiguration.mySite.GetLongitude(),
                      TimeZone, &nextsunrise, &nextsunset, &nextmoonrise, &nextmoonset);

      // check to see if the moon is up right now
      if(!isUp(sunset, moonrise, moonset))
      {
        fullmoon = false;
        // start at sunset
        start.tm_hour = (int) sunset;
        start.tm_min = (int) (sunset*60. - start.tm_hour*60.);
        start.tm_sec = (int) (sunset*3600. - start.tm_min*60. - start.tm_hour*3600.);

        if(moonrise > 12)
        {
          // stop at moonrise
          stop.tm_hour = (int) moonrise;
          stop.tm_min = (int) (moonrise*60. - stop.tm_hour*60.);
          stop.tm_sec = (int) (moonrise*3600. - stop.tm_min*60. - stop.tm_hour*3600.);
        } else
        {
          // stop tomorrow
          stop.tm_mday++;

          if(nextsunrise < nextmoonrise)
          {
            // stop at sunrise
            stop.tm_hour = (int) nextsunrise;
            stop.tm_min = (int) (nextsunrise*60. - stop.tm_hour*60.);
            stop.tm_sec = (int) (nextsunrise*3600. - stop.tm_min*60. - stop.tm_hour*3600.);
          } else
          {
            // stop at moonrise
            stop.tm_hour = (int) nextmoonrise;
            stop.tm_min = (int) (nextmoonrise*60. - stop.tm_hour*60.);
            stop.tm_sec = (int) (nextmoonrise*3600. - stop.tm_min*60. - stop.tm_hour*3600.);
          }
        }
      } else if(moonset > sunset)
      {
        fullmoon = false;

        // start at moonset today
        start.tm_hour = (int) moonset;
        start.tm_min = (int) (moonset*60. - start.tm_hour*60.);
        start.tm_sec = (int) (moonset*3600. - start.tm_min*60. - start.tm_hour*3600.);

        if(moonrise > moonset)
        {
          // stop at moonrise today
          stop.tm_hour = (int) moonrise;
          stop.tm_min = (int) (moonrise*60. - stop.tm_hour*60.);
          stop.tm_sec = (int) (moonrise*3600. - stop.tm_min*60. - stop.tm_hour*3600.);
        } else
        {
          // stop tomorrow
          stop.tm_mday++;

          if(nextsunrise < nextmoonrise)
          {
            // stop at sunrise
            stop.tm_hour = (int) nextsunrise;
            stop.tm_min = (int) (nextsunrise*60. - stop.tm_hour*60.);
            stop.tm_sec = (int) (nextsunrise*3600. - stop.tm_min*60. - stop.tm_hour*3600.);
          } else
          {
            // stop at moonrise
            stop.tm_hour = (int) nextmoonrise;
            stop.tm_min = (int) (nextmoonrise*60. - stop.tm_hour*60.);
            stop.tm_sec = (int) (nextmoonrise*3600. - stop.tm_min*60. - stop.tm_hour*3600.);
          }
        }
      } else if(nextmoonset < nextsunrise)
      {
        fullmoon = false;

        // start at moonset tomorrow morning
        start.tm_mday++;
        stop.tm_mday++;

        start.tm_hour = (int) nextmoonset;
        start.tm_min = (int) (nextmoonset*60. - start.tm_hour*60.);
        start.tm_sec = (int) (nextmoonset*3600. - start.tm_min*60. - start.tm_hour*3600.);

        if(nextsunrise < nextmoonrise)
        {
          // stop at sunrise
          stop.tm_hour = (int) nextsunrise;
          stop.tm_min = (int) (nextsunrise*60. - stop.tm_hour*60.);
          stop.tm_sec = (int) (nextsunrise*3600. - stop.tm_min*60. - stop.tm_hour*3600.);
        } else
        {
          // stop at moonrise
          stop.tm_hour = (int) nextmoonrise;
          stop.tm_min = (int) (nextmoonrise*60. - stop.tm_hour*60.);
          stop.tm_sec = (int) (nextmoonrise*3600. - stop.tm_min*60. - stop.tm_hour*3600.);
        }
      }

      // see if we are after the last image
      temp_tm = stop;
      temp_tm.tm_mday+=extra_day;
      if(time(NULL) > mktime(&temp_tm))
        fullmoon = true;

      extra_day++;
    }
  }
  else
  {
    // Get the rise and set times for the sun and the moon for today
    GetRiseSetTimes(LT.tm_mon, LT.tm_mday + extra_day, LT.tm_year,
		      myLatitude, myLongitude,
//                      mySystem.myConfiguration.mySite.GetLatitude(),
//                      mySystem.myConfiguration.mySite.GetLongitude(),
                      TimeZone, &sunrise, &sunset, &moonrise, &moonset);

    // Get the rise and set times for the sun and the moon for tomorrow
    GetRiseSetTimes(LT.tm_mon, LT.tm_mday + 1 + extra_day, LT.tm_year,
		      myLatitude, myLongitude,
//                      mySystem.myConfiguration.mySite.GetLatitude(),
//                      mySystem.myConfiguration.mySite.GetLongitude(),
                      TimeZone, &nextsunrise, &nextsunset, &nextmoonrise, &nextmoonset);

    // start at sunset
    start.tm_hour = (int) sunset;
    start.tm_min = (int) (sunset*60. - start.tm_hour*60.);
    start.tm_sec = (int) (sunset*3600. - start.tm_min*60. - start.tm_hour*3600.);

    // stop at sunrise
    stop.tm_hour = (int) nextsunrise;
    stop.tm_min = (int) (nextsunrise*60. - stop.tm_hour*60.);
    stop.tm_sec = (int) (nextsunrise*3600. - stop.tm_min*60. - stop.tm_hour*3600.);

    // stop tomorrow
    stop.tm_mday++;

    extra_day++;
  }

  // add in the extra days
  start.tm_mday += extra_day - 1;
  stop.tm_mday += extra_day - 1;

  // Correct the yday and mday entries in the tm structures
  mktime(&start);
  mktime(&stop);
  
  myStartTime = start;
  myStopTime = stop;
  
  // Make a note of the start and stop times in the system log
  string str("Auto set start time to: ");
  char time_string[64];
  strftime(time_string, 64, "%a %b %d %H:%M:%S %Y", &myStartTime);
  str = str + time_string;
  mySystem.myConfiguration.myLogger.WriteSystemLogString(str);

  string str2("Auto set stop time to: ");
  strftime(time_string, 64, "%a %b %d %H:%M:%S %Y", &myStopTime);
  str2 = str2 + time_string;
  mySystem.myConfiguration.myLogger.WriteSystemLogString(str2);

  // Set the sun/moon rise/set times
  SetTodaysRiseSetTimes();

  // Save the XML configuration file
  string myString;
  myString = "Writing XML file: " + mySystem.myConfiguration.myDirectories.GetQuickLookPath() + mySystem.myXMLFilename;
  mySystem.myConfiguration.myLogger.WriteSystemLogString(myString);
  mySystem.myConfiguration.SaveXML(mySystem.myConfiguration.myDirectories.GetQuickLookPath() + mySystem.myXMLFilename);
  
  return true;
}
/** Converts from degrees to radians */
double Schedule::DegRad(float Degrees){
  double pi = atan(1.f) * 4.f;
  return(Degrees * pi / 180.);
}
/** Sets the schedule mode */
void Schedule::SetScheduleMode(int mode){
  myScheduleMode = mode;

  string str("Set Schedule mode to ");
  if(myScheduleMode == SCHEDULE_OFF)
    str = str + "OFF";
  else if(myScheduleMode == SCHEDULE_AUTO)
    str = str + "AUTO";
  else if(myScheduleMode == SCHEDULE_MANUAL)
    str = str + "MANUAL";
  else
  {
    str = str + "???";
    mySystem.myConfiguration.myLogger.WriteErrorString(str);
  }

  mySystem.myConfiguration.myLogger.WriteSystemLogString(str);

  // If the mode is set to Auto, automatically set the start and stop times
//  if(myScheduleMode == SCHEDULE_AUTO)
//    AutoSetTimes();
}
/** returns the schedulemode flag */
int Schedule::GetScheduleMode(){
  return myScheduleMode;
}
/** No descriptions */
void Schedule::WriteXML(ofstream &os){
  // Put the header label
  os << "<schedule>" << endl;

  // Write the angles
  os << "<moonangle>" << myMoonAngle << "</moonangle>" << endl;
  os << "<sunangle>" << mySunAngle << "</sunangle>" << endl;

  // Write the flags
  os << "<moonset>" << myMoonSet << "</moonset>" << endl;
  os << "<schedulemode>" << myScheduleMode << "</schedulemode>" << endl;

  // Write moon/sun rise/set times
  char time_string[64];
  strftime(time_string, 64, "%a %b %d %H:%M:%S %Y", &mySunRiseTime);
  os << "<sunrisetime>" << time_string << "</sunrisetime>" << endl;
  strftime(time_string, 64, "%a %b %d %H:%M:%S %Y", &mySunSetTime);
  os << "<sunsettime>" << time_string << "</sunsettime>" << endl;
  strftime(time_string, 64, "%a %b %d %H:%M:%S %Y", &myMoonRiseTime);
  os << "<moonrisetime>" << time_string << "</moonrisetime>" << endl;
  strftime(time_string, 64, "%a %b %d %H:%M:%S %Y", &myMoonSetTime);
  os << "<moonsettime>" << time_string << "</moonsettime>" << endl;
  strftime(time_string, 64, "%a %b %d %H:%M:%S %Y", &myStartTime);
  os << "<starttime>" << time_string << "</starttime>" << endl;  
  strftime(time_string, 64, "%a %b %d %H:%M:%S %Y", &myStopTime);
  os << "<stoptime>" << time_string << "</stoptime>" << endl; 

  os << "</schedule>" << endl;
}
/** No descriptions */
void Schedule::SetTodaysRiseSetTimes(){

  time_t UT_time, LT_time;
  UT_time = time(NULL);
  LT_time = time(NULL);

  struct tm LT;
  struct tm UT;

  // Get the current LT and UT
  UT = *gmtime(&UT_time);
  LT = *localtime(&LT_time);

  struct tm start = LT;
  struct tm stop = LT;
  struct tm temp_tm;

  double sunrise, sunset, moonrise, moonset;
  double nextsunrise, nextsunset, nextmoonrise, nextmoonset;

  int extra_day = 0;
  bool fullmoon = true;

  int GMTHour = UT.tm_hour;
  int LTHour = LT.tm_hour;
  int TimeZone = ((GMTHour - LTHour) + 24) % 24;

  mySunRiseTime = LT;
  mySunSetTime = LT;
  myMoonRiseTime = LT;
  myMoonSetTime = LT;

  mySunAndMoon.m_MoonAngle = DegRad(0.);
  mySunAndMoon.m_SunAngle = DegRad(18.);

  // Get the rise and set times for the sun and the moon for today
  GetRiseSetTimes(LT.tm_mon, LT.tm_mday + extra_day, LT.tm_year,
		  myLatitude, myLongitude,
//                  mySystem.myConfiguration.mySite.GetLatitude(),
//                  mySystem.myConfiguration.mySite.GetLongitude(),
                  TimeZone, &sunrise, &sunset, &moonrise, &moonset);

  // Set the sunrise and sunset times
  mySunRiseTime.tm_hour = (int) sunrise;
  mySunRiseTime.tm_min = (int) (sunrise*60. - mySunRiseTime.tm_hour*60.);
  mySunRiseTime.tm_sec = (int) (sunrise*3600. - mySunRiseTime.tm_min*60. - mySunRiseTime.tm_hour*3600.);
  mySunSetTime.tm_hour = (int) sunset;
  mySunSetTime.tm_min = (int) (sunset*60. - mySunSetTime.tm_hour*60.);
  mySunSetTime.tm_sec = (int) (sunset*3600. - mySunSetTime.tm_min*60. - mySunSetTime.tm_hour*3600.);
  myMoonRiseTime.tm_hour = (int) moonrise;
  myMoonRiseTime.tm_min = (int) (moonrise*60. - myMoonRiseTime.tm_hour*60.);
  myMoonRiseTime.tm_sec = (int) (moonrise*3600. - myMoonRiseTime.tm_min*60. - myMoonRiseTime.tm_hour*3600.);
  myMoonSetTime.tm_hour = (int) moonset;
  myMoonSetTime.tm_min = (int) (moonset*60. - myMoonSetTime.tm_hour*60.);
  myMoonSetTime.tm_sec = (int) (moonset*3600. - myMoonSetTime.tm_min*60. - myMoonSetTime.tm_hour*3600.);
}
