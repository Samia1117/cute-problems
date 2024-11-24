class Logger {

    private final HashMap<String, Integer> msgToTsMap;

    public Logger() {
        this.msgToTsMap = new HashMap<>();
    }
    
    public boolean shouldPrintMessage(int timestamp, String message) {

        if (message == null) {
            return false;
        }

        if (!msgToTsMap.containsKey(message)) {
            msgToTsMap.put(message, timestamp);
            return true;
        } else {
            int lastPrinted = msgToTsMap.get(message);
            if (lastPrinted <= timestamp - 10) {
                msgToTsMap.put(message, timestamp);
                return true;
            } else {
                // Not printing this time, so no need to update the timestamp
                // msgToTsMap.put(message, timestamp);
                return false;
            }
        }
        
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */
