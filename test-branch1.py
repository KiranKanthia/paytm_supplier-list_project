from pyrfc import Connection

# Connection parameters (replace with your SAP system details)
conn_params = {
    'user': 'SAP_USER',
    'passwd': 'SAP_PASSWORD',
    'ashost': 'SAP_SERVER_HOST',
    'sysnr': '00',          # SAP system number
    'client': '100',        # SAP client
    'lang': 'EN'
}

# Establish connection
conn = Connection(**conn_params)

# Example: Call a standard SAP function module (RFC_READ_TABLE)
result = conn.call('RFC_READ_TABLE',
                   QUERY_TABLE='MARA',   # Material master table
                   DELIMITER='|',
                   ROWCOUNT=10)

# Print results
for row in result['DATA']:
    print(row['WA'])
