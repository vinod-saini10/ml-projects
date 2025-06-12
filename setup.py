from setuptools import find_packages, setup
from typing import List



HYPEN_E_DOT='e .'
def get_requirements(file_path: str) -> List[str]:
 '''
 this function will return the list of requirements
 '''

 
 with open(file_path) as file_obj:
   requirements=file_obj.readlines()
   [req.strip() for req in requirements if req.strip()!= HYPEN_E_DOT]

  
 return requirements


setup(
name='mlprojects',
version='0.0.1',
author='Vinod',
author_email='vinodsaini.bit@gmail.com',
package=find_packages(),
install_requires= get_requirements('requirements.txt')

)