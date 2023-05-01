import os
import oci
import time
import logging
from dotenv import load_dotenv

load_dotenv()


SSH_AUTHORIZED_KEYS = os.getenv("SSH_AUTHORIZED_KEYS")
IMAGE_ID = os.getenv("IMAGE_ID")
SUBNET_ID = os.getenv("SUBNET_ID")
AVAILABILITY_DOMAIN =os.getenv("AVAILABILITY_DOMAIN")
COMPARTMENT_ID = os.getenv("COMPARTMENT_ID")
SHAPE = "VM.Standard.A1.Flex"
SLEEP_TIME = 100


config_from_file = oci.config.from_file()
oci.base_client.is_http_log_enabled(True)
logging.getLogger('oci').setLevel(logging.DEBUG)


meta_data = {"ssh_authorized_keys": SSH_AUTHORIZED_KEYS}

shape_config = oci.core.models.LaunchInstanceShapeConfigDetails(
	ocpus=2,
	memory_in_gbs=12,
)

source_details = oci.core.models.InstanceSourceViaImageDetails(
	boot_volume_size_in_gbs=50,
	image_id=IMAGE_ID,
	source_type="image",
)

create_vnic_details = oci.core.models.CreateVnicDetails(
	assign_private_dns_record=True,
	assign_public_ip=True,
	subnet_id=SUBNET_ID,
)

launch_instance_details = oci.core.models.LaunchInstanceDetails(
	availability_domain=AVAILABILITY_DOMAIN,
	compartment_id=COMPARTMENT_ID,
	shape=SHAPE,
	shape_config=shape_config,
	metadata=meta_data,
	source_details=source_details,
	create_vnic_details=create_vnic_details
)

if __name__ == "__main__":
	client = oci.core.ComputeClient(config_from_file)

	while True:
		try:
			instance = client.launch_instance(launch_instance_details=launch_instance_details)
			logging.info("Success! %s", instance)
			break
		except oci.exceptions.ServiceError as err:
			logging.error("Error! %s, waiting %s seconds", err, SLEEP_TIME)
			time.sleep(SLEEP_TIME)
