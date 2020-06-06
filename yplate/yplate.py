import argparse
from yplate.commands import detect,crop
from yplate.ops import model_config,display_top,load_model

version = '0.0.1'

def main():
	parser = argparse.ArgumentParser(description="Detect car/vehicle number plates from any image or video files by using the following commands")
	subparser = parser.add_subparsers(title="commands", dest="command")

	#Version
	parser.add_argument('-v', action='version', version=version)


	"""  Detect Plate  """
	### 1. Detect Plate
	parser_detect = subparser.add_parser('detect',help = "Detect vehicle plates with this command ")
	parser_detect.add_argument('inp',type= str)

	### 1.a Save output (optional with detect)
	parser_add = parser_detect.add_argument('--save',type = str,help = "Save the detected image/video in disk with a filename (default = original name)")

	### 1.b Hide detected image
	parser_show = parser_detect.add_argument('--hide_img',action='store_true',help = "Hide output image ")

	### 1.c Hide detected output
	parser_detect.add_argument('--hide_out',action='store_true',help = "Hide output in terminal")


	"""  Crop Plate  """
	### 2. Crop Plate	
	parser_crop = subparser.add_parser('crop',help = "Crop plates after detection")
	parser_crop.add_argument('inp',type = str)

	### 2.a Save output image (optional with crop)
	parser_crop.add_argument('--save',type = str,help = "Save the detected cropped plate in your disc")

	### 2.b Hide Output (optional with crop)
	parser_crop.add_argument('--hide_img',action='store_true',help = "Hide output image ")

	### 2.c Output (optional with crop)
	parser_crop.add_argument('--hide_out',action='store_true',help = "Hide output in terminal")


	""" Model Configuration """
	### 3. Model config
	parser.add_argument('--config',action='store_const', const=lambda:'model_config', dest='cmd')

	try:
		args = parser.parse_args()
		if (args.command == 'detect'):
			## Load model
			cfg,weights,classes = load_model()
			img = args.inp
			hide_img = args.hide_img
			save_img = args.save
			hide_out = args.hide_out

			if(args.save == None):
				save_img = True
				
			## Detect 
			detect(img,cfg,weights,classes,save_img,hide_img,hide_out)
			exit()
		elif(args.command == 'crop'):
			## Load model
			cfg,weights,classes = load_model()
			img = args.inp
			hide_img = args.hide_img
			save_img = args.save
			hide_out = args.hide_out
			if(args.save == None):
				save_img = True
			# Crop plate
			crop(img,cfg,weights,classes,save_img,hide_img,hide_out)
			exit()
		elif(args.cmd() == 'model_config'):
			## Display Model Config
			display_top()
			model_config()
			exit()
			

	except Exception as e:
		display_top()
		print("Command not found. Check the input commands again.\n For more info type 'yplate -h'")
		exit()

if __name__ == '__main__':
	main()
