# Environmental & Web Sensors

These sensors monitor the external digital architecture the agent navigates.

-   **DOM Tree Observer:** Tracks HTML changes in a web app to know when new content renders or elements disappear.
-   **API Response Listener:** Intercepts JSON/XML payloads from servers to ingest structured external data.
-   **Network Status Prober:** Monitors ping, bandwidth, and connection type (Wi-Fi/Cellular) to adjust data usage or handle offline modes.
-   **Cookie & LocalStorage Watcher:** Detects updates to browser storage to track session state changes or authentication tokens.
-   **URL/Route Monitor:** Tracks navigation path changes within a web or desktop app to know exactly which page the user is viewing.

# User Activity & Behavior Sensors

These sensors capture human interactions, allowing the agent to react, assist, or personalize experiences.

-   **Keystroke & Input Listener:** Captures text entry speed and specific key patterns to interpret user intent or detect typing fatigue.
-   **Mouse/Gesture Tracker:** Monitering coordinates, clicks, scrolls, and drag-and-drop actions to map user focus and frustration points.
-   **Window Focus (Blur) Sensor:** Detects when the user switches tabs or minimizes the application, telling the agent when to pause or alert.
-   **User Idle Timer:** Measures inactivity duration to trigger automatic logouts, save power, or offer proactive help.
-   **Biometric Feed Scanner:** Processes webcam facial expressions or microphone tone to gauge user emotion and frustration levels.

# Device Hardware & OS Sensors

These sensors bridge the gap between the software agent and the physical device running it.

-   **Battery & Power Monitor:** Tracks charging state and percentage to throttle heavy background processing when battery is low.
-   **CPU & RAM Load Sensor:** Measures hardware strain to prevent the agent from lagging the user's device.
-   **File System Watcher:** Monitors specific directories for file creation, edits, or deletions to trigger automation workflows.
-   **Location/GPS Sensor:** Feeds latitude, longitude, and altitude to the agent to provide localized context, currency, or time zones.
-   **OS Notification Listener:** Sniffs system-level alerts from other apps to integrate multi-app workflows.

# Internal State (Proprioceptive) Sensors

These sensors allow the agent to monitor its own digital "body," health, and operational logic.

-   **Execution Latency Timer:** Measures how long its own functions take to execute, sensing internal logic bottlenecks.
-   **Memory Leak Detector:** Monitors the agent's footprint over time to prevent crashes from excessive data accumulation.
-   **Exception/Error Catcher:** Instantly flags unhandled code exceptions or syntax crashes so the agent can initiate self-healing protocols.
-   **Token/Context Window Gauge:** Tracks how close an LLM-based agent is to filling its short-term memory limit.
-   **Queue Depth Counter:** Monitors pending tasks or message backlogs to sense if the agent is becoming overwhelmed by requests.