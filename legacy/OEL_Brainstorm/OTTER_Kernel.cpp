class OTTER_Kernel {
    public:
        OTTER_Scheduler scheduler;  // Create a scheduler instance
    
        // Add a task for I2C operation (e.g., sensor read or write)
        void addI2CTask(String sensorName, String operation, float value = 0) {
            scheduler.addTask(sensorName, operation, value);
        }
    
        // Execute tasks queued up in the scheduler
        void executeI2CTasks() {
            scheduler.executeTasks();
        }
    };