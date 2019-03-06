def get_query():
    """This function gets a hard coded KQL query to be executed 
	   against an ADX database.
	   
	   Parameters:
	   
	   None
	   
	   Returns:
      
	   string: A hard coded Kusto Query Language string
	   
    """
	
    return ('.show queries '
	        '| where Database == "TestDatabase" and State == "Completed" '
		    '| extend MilliSec = Duration / time(0.001s) '
		    '| summarize percentile(MilliSec, 50) by bin(StartedOn, 10000s) '
		   )
