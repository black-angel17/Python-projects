import pyshark
import csv
import concurrent.futures
# Open the pcap file
pcap_file = pyshark.FileCapture('test_data.pcap')
first_packet_time = None
for packet in pcap_file:
    first_packet_time = float(packet.sniff_timestamp)
    break  # Only need the first packet's timestamp
else:
    # If no packets were found, exit
    print("No packets found in the capture file.")
    exit()
# Initialize variables to track previous ACK number and timestamp
x = 1

output_csv_file = 'normal_details.csv'
with open('normal_details.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(
        ['Packet Number','Time(seconds)' ,'Time_interval', 'Layer','src_ip','scr_port','dst_port','ack_no','tcp_length','socket_count','sql','stream'])

    # Iterate through each packet in the pcap file
    while x < 4154:
        x = x+1
        prev_ack_number = None
        prev_timestamp = None
        for packet in pcap_file:
            # Check if the packet has TCP layer and source IP address
            if 'tcp' in packet and 'ip' in packet:
                src_ip = packet.ip.src
                stream = int(packet.tcp.stream)
                if src_ip == '192.168.136.131' and stream == x:
                    print(
                        f"Packet #{packet.number}: {stream}")
                    current_ack_number = int(packet.tcp.ack)

                    # Calculate the difference in ACK numbers between consecutive packets
                    if prev_ack_number is not None:
                        ack_difference = current_ack_number - prev_ack_number
                        if ack_difference < 0:
                            ack_difference = 0
                            # Access commonly used TCP fields
                        src_port = packet.tcp.srcport
                        dst_port = packet.tcp.dstport
                        seq_number = packet.tcp.seq
                        ack_number = packet.tcp.ack
                        window_size = packet.tcp.window_size
                        flags = packet.tcp.flags
                        data_length = packet.tcp.len

                        # Calculate time difference between consecutive packets (optional)
                        current_timestamp = float(packet.sniff_timestamp)
                        time_difference = current_timestamp - prev_timestamp
                        current_packet_time = float(packet.sniff_timestamp)
                        seconds_since_start = current_packet_time - first_packet_time
                        seconds = int(seconds_since_start)
                        flag1 = str(packet.tcp.flags_ack)
                        flag2 = str(packet.tcp.flags_push)
                        csvwriter.writerow(
                            [packet.number,seconds ,int(time_difference), packet.transport_layer, src_ip, src_port, dst_port,
                             ack_difference, data_length, socket, 0, stream])

                        # Update previous ACK number and timestamp for next iteration

                    prev_ack_number = current_ack_number
                    prev_timestamp = float(packet.sniff_timestamp)
                else:
                    pass

        else:
            prev_timestamps = None
            prev_ack_numbers = None

            for packet in pcap_file:
                # Check if the packet has TCP layer and source IP address
                if 'tcp' in packet and 'ip' in packet:
                    src_ip = packet.ip.src
                    stream = int(packet.tcp.stream)

                    # Assuming you want to track a specific source IP, you can use an if condition here

                    if src_ip != '192.168.136.131' and stream == x:
                        print(
                            f"Packet #{packet.number}: {stream}")
                        current_ack_numbers = int(packet.tcp.ack)

                            # Calculate the difference in ACK numbers between consecutive packets
                        if prev_ack_numbers is not None:
                            ack_differences = current_ack_numbers - prev_ack_numbers
                            if ack_differences < 0:
                                ack_differences = 0
                                # Access commonly used TCP fields
                            src_port = packet.tcp.srcport
                            dst_port = packet.tcp.dstport
                            seq_number = packet.tcp.seq
                            ack_number = packet.tcp.ack
                            window_size = packet.tcp.window_size
                            flags = packet.tcp.flags
                            data_length = packet.tcp.len


                            # Calculate time difference between consecutive packets (optional)
                            current_timestamps = float(packet.sniff_timestamp)
                            time_differences = current_timestamps - prev_timestamps
                            current_packet_time = float(packet.sniff_timestamp)
                            seconds_since_start = current_packet_time - first_packet_time
                            seconds = int(seconds_since_start)
                            flag1 = str(packet.tcp.flags_ack)
                            flag2 = str(packet.tcp.flags_push)

                            csvwriter.writerow([packet.number,seconds ,int(time_differences), packet.transport_layer,src_ip,src_port, dst_port,ack_differences, data_length,socket, 0,stream])

                            # Update previous ACK number and timestamp for next iteration

                        prev_ack_numbers = current_ack_numbers
                        prev_timestamps = float(packet.sniff_timestamp)
                    else:
                        pass
    # Close the pcap file

# At this point, all requests have been completed
print("All requests completed.")
pcap_file.close()
