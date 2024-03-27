% Enter your MATLAB Code below
readAPIKey = 'VYSA112AL9I8WAT2'; 
channelID = 2488423;       

% Fetch data from the last five hours
endDate = datetime('now', 'timezone', 'local');
startDate = endDate - hours(5);
[data, time] = thingSpeakRead(channelID, 'DateRange', [startDate, endDate], 'ReadKey', readAPIKey);

% Check if data is received
if ~isempty(data)
    disp("Data from Last 5 Hours:");
    
    % Assuming each row in 'data' corresponds to [Temperature, Humidity, CO2]
    for i = 1:size(data, 1)
        fprintf("Time: %s, ", datestr(time(i)));
        fprintf("Temperature: %.2f °C, ", data(i, 1));
        fprintf("Humidity: %.2f %%, ", data(i, 2));
        fprintf("CO2 Level: %.2f ppm\n", data(i, 3));
    end
else
    disp("No data received in the last 5 hours.");
end