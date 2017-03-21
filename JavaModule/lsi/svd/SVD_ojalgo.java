package svd;

import org.ojalgo.matrix.store.SparseStore;

import org.ojalgo.matrix.PrimitiveMatrix;
import org.ojalgo.matrix.decomposition.SingularValue;
import org.ojalgo.matrix.store.MatrixStore;
import org.ojalgo.matrix.store.PrimitiveDenseStore;

public class SVD_ojalgo {

	public static void main(String[] args) {
		
		/*
		
		UJMP: not stable but looks promising		
		
		ojalgo - no support of sparse matrices! Very complicated to use
		http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.ojalgo%22%20AND%20a%3A%22ojalgo%22
		Runtime comparison: http://lessthanoptimal.github.io/Java-Matrix-Benchmark/runtime/2015_07_XeonQuad/
		
		*/
		SparseStore<Double> sparse = SparseStore.PRIMITIVE.make(2, 2);
		sparse.set(0, 0, 1);		
		sparse.set(1, 1, 1);
		
		

		//PrimitiveMatrix m = PrimitiveMatrix.FACTORY.makeEye(500, 1000);		
				
		System.out.println(sparse.norm());
		
		SingularValue<Double> s = SingularValue.PRIMITIVE.make(sparse);
		s.decompose(sparse);
		/*[A] = [Q1][D][Q2]T Decomposes [this] into [Q1], [D] and [Q2] where:
			 [Q1] is an orthogonal matrix. The columns are the left, orthonormal, singular vectors of [this]. Its columns are the eigenvectors of [A][A]T, and therefore has the same number of rows as [this].
			 [D] is a diagonal matrix. The elements on the diagonal are the singular values of [this]. It is either square or has the same dimensions as [this]. The singular values of [this] are the square roots of the nonzero eigenvalues of [A][A]T and [A]T[A] (they are the same)
			 [Q2] is an orthogonal matrix. The columns are the right, orthonormal, singular vectors of [this]. Its columns are the eigenvectors of [A][A]T, and therefore has the same number of rows as [this] has columns.
			 [this] = [Q1][D][Q2]T*/
		MatrixStore<Double> d = s.getD();
		MatrixStore<Double> q1 = s.getQ1();
		MatrixStore<Double> q2 = s.getQ2();
		
		System.out.println("Q1:" + q1.countRows() + " x " + q1.countColumns() + "; norm: " + q1.norm());
		printMatrix(q1);
		System.out.println("D:" + d.countRows() + " x " + d.countColumns() + "; norm: " + d.norm());
		printMatrix(d);
		System.out.println("Q2:" + q2.countRows() + " x " + q2.countColumns() + "; norm: " + q2.norm());
		printMatrix(q2);
		
		
		
		

	}
	public static void printMatrix(MatrixStore<Double> m){
		String row = "";
		for (int i = 0; i < m.countRows(); i++) {
			row = "";
			for (int j = 0; j < m.countColumns(); j++) {
				row += m.get(i, j) + " ";				
			}
			System.out.println(row);
		}
	}

}
