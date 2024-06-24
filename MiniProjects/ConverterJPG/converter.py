import json

if __name__ == '__main__':
    try:
        with open('input.json', 'r') as f:
            data = json.load(f.read())

        output = ','.join([*data[0]])
        for obj in data:
            output += '\n' + ','.join([str(obj[key]) for key in obj])

        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as e:
        print(e)
        print('Error in converting JSON to CSV')