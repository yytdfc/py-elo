/////////////////////////////////////////////////////////////////////////////
//
// R�mi Coulom
//
// February, 2005
//
/////////////////////////////////////////////////////////////////////////////
#ifndef CMatrixIO_Declared
#define CMatrixIO_Declared

#include <iosfwd>

class CMatrix;

std::ostream &operator<<(std::ostream &out, const CMatrix &m);

#endif
