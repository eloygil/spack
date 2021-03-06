##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RAbind(RPackage):
    """Combine multidimensional arrays into a single array. This is a
    generalization of 'cbind' and 'rbind'. Works with vectors, matrices, and
    higher-dimensional arrays. Also provides functions 'adrop', 'asub', and
    'afill' for manipulating, extracting and replacing data in arrays."""

    homepage = "https://cran.r-project.org/"
    url      = "https://cran.r-project.org/src/contrib/abind_1.4-3.tar.gz"

    version('1.4-3', '10fcf80c677b991bf263d38be35a1fc5')
