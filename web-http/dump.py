import pyshark
import csv
# Open the pcap file
pcap_file = pyshark.FileCapture('test1.pcap')

# Get the timestamp of the first packet
first_packet_time = None
for packet in pcap_file:
    first_packet_time = float(packet.sniff_timestamp)
    break  # Only need the first packet's timestamp
else:
    # If no packets were found, exit
    print("No packets found in the capture file.")
    exit()

# Reset the file capture to read from the beginning again
pcap_file.close()
pcap_file = pyshark.FileCapture('test1.pcap')
# Define the name for the output CSV file
output_csv_file = 'packet_details.csv'
with open('packet_details.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(
        ['Packet Number', 'Time (seconds)', 'Layer','src_ip','dst_ip','scr_port','dst_port','ack_no','tcp_length','window_size','sql'])

    # Loop through each packet in the pcap file
    for packet in pcap_file:
        src_ip = None
        dst_ip = None
        src_port = None
        dst_port = None
        ack_no = None
        tcp_length = None
        window_size = None
        # Calculate the time difference in seconds from the first packet
        current_packet_time = float(packet.sniff_timestamp)
        seconds_since_start = current_packet_time - first_packet_time

        packet_no = packet.number
        seconds = seconds_since_start
        # Print packet summary
        print(f"Packet #{packet.number}: {seconds_since_start:.2f} seconds  {packet.length} bytes")

        # Print packet details

        for layer in packet.layers:
            print(f"Layer: {layer.layer_name}")


            if layer.layer_name == 'ip':
                src_ip = layer.src_host
                dst_ip = layer.dst_host

            elif layer.layer_name == 'tcp':

                src_port =getattr(layer, 'srcport')
                dst_port = getattr(layer, 'dstport')
                ack_no = getattr(layer, 'ack')
                tcp_length =getattr(layer, 'len')
                window_size = getattr(layer, 'window_size')

                print(f"\t{'srcport'}: {getattr(layer, 'srcport')}")
                print(f"\t{'dstport'}: {getattr(layer, 'dstport')}")
                print(f"\t{'ack'}: {getattr(layer, 'ack')}")
                print(f"\t{'tcp_length'}: {getattr(layer, 'len')}")
                print(f"\t{'window_size'}: {getattr(layer, 'window_size')}")
                print(f"\t{'time interval'}: {int(float(layer.time_delta))}")
                print("------------------------------------------------------")
                csvwriter.writerow(
                    [packet_no, seconds, packet.transport_layer, src_ip, dst_ip, src_port, dst_port, ack_no, tcp_length,
                     window_size, 1])



            else:
                pass

# Close the pcap file
pcap_file.close()

print(f"CSV file '{output_csv_file}' has been generated.")

# Loop through each layer in the packet
for layer in packet.layers:
    if layer.layer_name == 'ip':
        src_ip = layer.ip.src
        dst_ip = layer.ip.dst
    elif layer.layer_name == 'tcp':
        src_port = layer.tcp.srcport
        dst_port = layer.tcp.dstport
        ack_no = layer.tcp.ack
        tcp_length = layer.length
        window_size = layer.tcp.window_size




        if layer.layer_name == 'tcp':

            src_port = int(getattr(layer, 'stream'))

            if src_port == 115 :

                print(f"Packet #{packet.number}: {seconds_since_start:.2f} seconds {packet.transport_layer} {packet.length} bytes")
                print(f"\t{'srcport'}: {getattr(layer, 'srcport')}")
                print(f"\t{'dstport'}: {getattr(layer, 'dstport')}")
                print(f"\t{'stream'}: {getattr(layer, 'stream')}")
                print(f"\t{'ack'}: {getattr(layer, 'ack')}")
                print(f"\t{'tcp_length'}: {getattr(layer, 'len')}")
                print(f"\t{'window_size'}: {getattr(layer, 'window_size')}")
                print(f"\t{'time interval'}: {int(float(layer.time_delta))}")
                print("------------------------------------------------------")









import pyshark

# Open the pcap file
pcap_file = pyshark.FileCapture('test1.pcap')

# Initialize variables to track previous ACK number and timestamp
prev_ack_number = None
prev_timestamp = None

# Iterate through each packet in the pcap file
for packet in pcap_file:
    # Check if the packet has TCP layer and source IP address
    if 'tcp' in packet and 'ip' in packet:
        src_ip = packet.ip.src
        stream = int(packet.tcp.stream)

        # Assuming you want to track a specific source IP, you can use an if condition here
        if src_ip == '192.168.77.106' and stream == 5:
            print(
                f"Packet #{packet.number}: {packet.transport_layer} {packet.length} bytes")
            current_ack_number = int(packet.tcp.ack)



            # Calculate the difference in ACK numbers between consecutive packets
            if prev_ack_number is not None:
                ack_difference = current_ack_number - prev_ack_number

                # Calculate time difference between consecutive packets (optional)
                current_timestamp = float(packet.sniff_timestamp)
                time_difference = current_timestamp - prev_timestamp

                print(f"ACK Difference: {ack_difference}, Time Difference: {time_difference:.6f} seconds, stream: {stream}")

            # Update previous ACK number and timestamp for next iteration
            prev_ack_number = current_ack_number
            prev_timestamp = float(packet.sniff_timestamp)

# Close the pcap file
pcap_file.close()

print(f"Source Port: {src_port}, Destination Port: {dst_port}")
print(f"ACK Difference: {ack_difference}, Time Difference: {int(time_difference):} seconds, stream: {stream}")
print(f"Window Size: {window_size}, Flags: {flags}, Data Length: {data_length}")
print("source ip" + src_ip)