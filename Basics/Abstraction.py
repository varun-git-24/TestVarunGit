# from abc import ABC, abstractmethod
#
#
# class MainClass(ABC):
#     def __init__(self, place):
#         self.place = place
#
#     @abstractmethod
#     def expected_scenes(self):
#         pass
#
#
# class Beach(MainClass):
#     def __init__(self, *places):
#         super().__init__('Goa')
#         self.places = places
#
#     def expected_scenes(self):
#         for item in self.places:
#             print(f'Places to visit in {self.place} are - {item}')
#         return ''
#
#
# class Temple(MainClass):
#     def __init__(self, *places):
#         super().__init__('Karnataka')
#         self.places = places
#
#     def expected_scenes(self):
#         for item in self.places:
#             print(f'Places to visit in {self.place} are - {item}')
#         return ''
#
#
# place_obj = Beach('Sea', 'Church', 'Paniji')
# print(place_obj.expected_scenes())


#m = ["sed -i -e 's/$PROFILE/CU_VM_PROFILE_MACRO_4G_12CELLS_8VCPU_700UES_20MHZ_4X4/g' values.yaml", "sed -i -e 's/$CU_NODE_SELECTOR/\\trpoolName: 'default'/g' values.yaml", "sed -i -e 's/$NAME_PREFIX/NGDU35/g' values.yaml", "sed -i -e 's/$STORAGE_CLASS_NAME/robin/g' values.yaml", "sed -i -e 's/$VRAN_ENB_ID/11081/g' values.yaml", "sed -i -e 's/$VRAN_NF_ID/81/g' values.yaml", "sed -i -e 's/$VRAN_NF_ID/81/g' values.yaml", "sed -i -e 's/$HOST_NAME/uhn1tky900400018cu.nfbulab.com/g' values.yaml", "sed -i -e 's/$FQDN/uhn1tky900400018cu.nfbulab.com/g' values.yaml", "sed -i -e 's/$TIMEZONE/ASIA/KOLKATA/g' values.yaml", "sed -i -e 's/$NW_TYPE/v6/g' values.yaml", "sed -i -e 's/$EMS_FQDN/c9robin13ems-oss-ha.nfbulab.com/g' values.yaml", "sed -i -e 's/$EMS_SNMP_PORT/1622/g' values.yaml", "sed -i -e 's/$MH_DATA_IPSEC/enabled/g' values.yaml", "sed -i -e 's/$CA_FQDN/fd02:298c:8dfe:357:1:1:1:2001/g' values.yaml", "sed -i -e 's/$CA_PORT/8081/g' values.yaml", "sed -i -e 's/$TLS_SRP_USERNAME/altiostar/g' values.yaml", "sed -i -e 's/$TLS_SRP_PASSWORD/altiostar/g' values.yaml", "sed -i -e 's/$VRAN_CU_CORRELATION_ID/id1,id2,id3/g' values.yaml", 'sed -i -e \'s/$VRAN_CU_LABELS/VENDOR:"ALTIOSTAR"\\n\\tGROUP:"RAN"/g\' values.yaml', "sed -i -e 's/$MGMT_IPPOOL/mgmt-nw/g' values.yaml", "sed -i -e 's/$MH_IPPOOL/vcu-mhc/g' values.yaml", "sed -i -e 's/$BH_S1_IPPOOL/s1u-nw/g' values.yaml", "sed -i -e 's/$MGMT_IP/fd10:298c:8dfe:0811:0000:00c8:0002:2008/g' values.yaml", "sed -i -e 's/$MH_IP/fd10:298c:8dfe:0814:0000:10c8:0002:4008/g' values.yaml", "sed -i -e 's/$BH_S1_IP/fd10:298c:8dfe:0826:0000:00c8:0002:2008/g' values.yaml"]
m = ["sed -i -e 's/$PROFILE/CU_VM_PROFILE_MACRO_4G_12CELLS_8VCPU_700UES_20MHZ_4X4/g' values.yaml", "sed -i -e 's/$CU_NODE_SELECTOR/\\trpoolName: 'default'/g' values.yaml", "sed -i -e 's/$NAME_PREFIX/NGDU35/g' values.yaml", "sed -i -e 's/$STORAGE_CLASS_NAME/robin/g' values.yaml", "sed -i -e 's/$VRAN_ENB_ID/11081/g' values.yaml", "sed -i -e 's/$VRAN_NF_ID/81/g' values.yaml", "sed -i -e 's/$VRAN_NF_ID/81/g' values.yaml", "sed -i -e 's/$HOST_NAME/uhn1tky900400018cu.nfbulab.com/g' values.yaml", "sed -i -e 's/$FQDN/uhn1tky900400018cu.nfbulab.com/g' values.yaml", "sed -i -e 's/$TIMEZONE/ASIA/KOLKATA/g' values.yaml", "sed -i -e 's/$NW_TYPE/v6/g' values.yaml", "sed -i -e 's/$EMS_FQDN/c9robin13ems-oss-ha.nfbulab.com/g' values.yaml", "sed -i -e 's/$EMS_SNMP_PORT/1622/g' values.yaml", "sed -i -e 's/$MH_DATA_IPSEC/enabled/g' values.yaml", "sed -i -e 's/$CA_FQDN/fd02:298c:8dfe:357:1:1:1:2001/g' values.yaml", "sed -i -e 's/$CA_PORT/8081/g' values.yaml", "sed -i -e 's/$TLS_SRP_USERNAME/altiostar/g' values.yaml", "sed -i -e 's/$TLS_SRP_PASSWORD/altiostar/g' values.yaml", "sed -i -e 's/$VRAN_CU_CORRELATION_ID/id1,id2,id3/g' values.yaml", 'sed -i -e \'s/$VRAN_CU_LABELS/VENDOR:"ALTIOSTAR"\\n\\tGROUP:"RAN"/g\' values.yaml', "sed -i -e 's/$MGMT_IPPOOL/mgmt-nw/g' values.yaml", "sed -i -e 's/$MH_IPPOOL/vcu-mhc/g' values.yaml", "sed -i -e 's/$BH_S1_IPPOOL/s1u-nw/g' values.yaml", "sed -i -e 's/$MGMT_IP/fd10:298c:8dfe:0811:0000:00c8:0002:2008/g' values.yaml", "sed -i -e 's/$MH_IP/fd10:298c:8dfe:0814:0000:10c8:0002:4008/g' values.yaml", "sed -i -e 's/$BH_S1_IP/fd10:298c:8dfe:0826:0000:00c8:0002:2008/g' values.yaml"]
#x = []
m = [item for item in m]

for item in m:
    print(item)

#print(m)



