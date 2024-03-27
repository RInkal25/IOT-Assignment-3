% Enter your MATLAB Code below
readAPIKey = 'VYSA112AL9I8WAT2';  
channelID = 2488423;             

% Fetch the latest data
[data, time] = thingSpeakRead(channelID, 'ReadKey', readAPIKey, 'NumPoints', 1);

% Assuming data format is [Temperature, Humidity, CO2]
if ~isempty(data)
    temperature = data(1);
    humidity = data(2);
    co2 = data(3);

    disp("Latest Data: ");
    fprintf("Time: %s\n", datestr(time));
    fprintf("Temperature: %.2f °C\n", temperature);
    fprintf("Humidity: %.2f %%\n", humidity);
    fprintf("CO2 Level: %.2f ppm\n", co2);
else
    disp("No data received.");
end   