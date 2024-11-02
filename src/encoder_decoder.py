import struct

wind_directions = {
    'N': 0, 'NE': 1, 'E': 2, 'SE': 3, 'S': 4, 'SW': 5, 'W': 6, 'NW': 7
}

class EncoderDecoder():
    def encode(self, x) -> bytes:
        #reduce to 10 bits and limit to 0-1023 range with one decimal
        temperature = min(max(int(x['temperature'] * 10), 0), 1023)
        # reduce to 7 bits and limit to 0-127 range
        humidity = min(max(x['humidity'], 0), 127)
        # reduce to 3 bits and limit to 0-7 range
        wind_direction = wind_directions.get(x['wind_direction'], 0)
        
        # Encode data
        encoded_data = (temperature << 10) | (humidity << 3) | wind_direction
        res = struct.pack('>I', encoded_data)[1:]

        return res # return the encoded data

    def decode(self, x) -> dict:
        unpacked = struct.unpack('>I', b'\x00' + x)[0]
        temperature = ((unpacked >> 10) & 0x3FF) / 10.0
        humidity = (unpacked >> 3) & 0x7F
        wind_direction_code = unpacked & 0x07
        
        # Decode data
        wind_direction = [k for k, v in wind_directions.items() if v == wind_direction_code][0]
        
        return {
            'temperature': temperature,
            'humidity': humidity,
            'wind_direction': wind_direction
        }
    
    def sizeOf(self, x) -> int:
        #return the size of the encoded data
        return len(x)